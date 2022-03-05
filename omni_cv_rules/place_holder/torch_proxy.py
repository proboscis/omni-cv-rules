class RealTorchProxy:
    @property
    def torch(self):
        import torch
        return torch

    def from_numpy(self, ary):
        return self.torch.from_numpy(ary)
    def cat(self,ary,dim):
        return self.torch.cat(ary,dim)
    def tensor(self,ary):
        return self.torch.tensor(ary)

torch = RealTorchProxy()


