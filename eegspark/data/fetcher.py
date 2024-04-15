from mne import create_info
from mne.io import RawArray, read_raw_bdf, read_raw_edf, read_raw_fif, read_raw_eeglab, read_raw_brainvision, \
    read_raw_gdf
from mne.channels import make_standard_montage
import numpy as np
import scipy.io as sio
import os
class Source:
    def __init__(self, target: str) -> None:
        self.target = target
    # Load data based on file type
    def load_data(self) -> RawArray:
        file_extension = os.path.splitext(self.target)[1].lower()
        # Update loaders dictionary to include GDF loader
        loaders = {
            '.mat': self._load_data_from_mat,
            '.bdf': read_raw_bdf,
            '.edf': read_raw_edf,
            '.fif': read_raw_fif,
            '.vhdr': read_raw_brainvision,
            '.set': read_raw_eeglab,
            '.gdf': read_raw_gdf,  # Add this line for handling .gdf files
            # Add other supported file types and their corresponding loading functions if necessary
        }
        loader = loaders.get(file_extension)
        if loader is not None:
            if file_extension == '.mat':
                # 这里移除了preload参数，因为它不应该被传入_load_data_from_mat
                return self._load_data_from_mat()
            else:
                # 对于其他文件类型，保持原来的调用方式，包括preload参数
                return loader(self.target, preload=True)
            # ...省略其他逻辑...
        else:
            raise ValueError(f"Unsupported file type: {file_extension}")
    def _load_data_from_mat(self) -> RawArray:
        # Load EEG data from a .mat file
        mat = sio.loadmat(self.target)
        eeg_data = mat["data"][:, :-1]
        num_channels = eeg_data.shape[1]
        # Set up channel names and types
        eeg_channels = ["EEG {:03d}".format(i + 1) for i in range(num_channels)]
        ch_types = ["eeg"] * num_channels + ["stim"]
        ch_names = eeg_channels + ["STI 014"]
        info = create_info(ch_names=ch_names, sfreq=500, ch_types=ch_types)
        # Transpose data to match MNE expectations and add stimulus channel
        eeg_data = eeg_data.T
        stim_data = mat["data"][:, -1].reshape(1, -1)
        data = np.concatenate([eeg_data, stim_data], axis=0)
        raw = RawArray(data=data, info=info)
        # Set up standard montage and ignore missing channels
        montage = make_standard_montage("standard_1020")
        raw.set_montage(montage, on_missing="ignore")
        return raw