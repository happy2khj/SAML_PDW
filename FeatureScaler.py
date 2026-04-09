from utilityProc import utilityProc
import torch

class FeatureScaler:

    def __init__(self, mode: str="standard"):
        self.mode = mode

    def transform(self, X):

        continuous = X[:, :6]
        signal_type = X[:, 6:7]

        if self.mode == "standard":

            mean = continuous.mean(dim=0, keepdim=True)
            std = continuous.std(dim=0, keepdim=True)

            scaled = (continuous - mean) / (std + 1e-8)

        elif self.mode == "robust":

            median = continuous.median(dim=0, keepdim=True).values

            q1 = continuous.quantile(0.25, dim=0, keepdim=True)
            q3 = continuous.quantile(0.75, dim=0, keepdim=True)

            iqr = q3 - q1

            scaled = (continuous - median) / (iqr + 1e-8)

        else:
            raise ValueError("unknown mode")

        return torch.cat([scaled, signal_type], dim=1)