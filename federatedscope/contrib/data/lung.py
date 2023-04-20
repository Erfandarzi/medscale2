import os
import numpy as np
import torch
from torchvision.datasets import ImageFolder, VisionDataset
from torch import device
from torch.utils.data import DataLoader 
from torchvision import datasets, transforms
from federatedscope.register import register_data

# Run with mini_graph_dt:
# python federatedscope/main.py --cfg \
# federatedscope/gfl/baseline/mini_graph_dc/fedavg.yaml --client_cfg \
# federatedscope/gfl/baseline/mini_graph_dc/fedavg_per_client.yaml
# Test Accuracy: ~0.7

    

   
<<<<<<< HEAD
def load_my_data(config, client_cfgs=None):
      from federatedscope.core.data import BaseDataTranslator


      # class lungdataset(VisionDataset):

            
      #       def __init__(self, root, splits=[0.8, 0.1, 0.1]):
      #             self.root = root
      #             self.splits = splits
      #             super(lungdataset, self).__init__(root)
      
      #       def __getitem__(self, index: int) -> Tuple[Any, Any]:
      #       """
      #       Args:
      #             index (int): Index
      #       Returns:
      #             tuple: (image, target) where target is index of the target class.
      #       """
      #       img, target = self.data[index], self.targets[index]

      #       # doing this so that it is consistent with all other datasets
      #       # to return a PIL Image
      #       img = Image.fromarray(img)

      #       if self.transform is not None:
      #             img = self.transform(img)

      #       if self.target_transform is not None:
      #             target = self.target_transform(target)

      #       return img, target

      # def __len__(self) -> int:
      #       return len(self.data)



      transform=transforms.Compose([
        transforms.RandomRotation(10),      # rotate +/- 10 degrees
        transforms.RandomHorizontalFlip(),  # reverse 50% of images
        transforms.Resize(100),             # resize shortest side
        transforms.CenterCrop(100),   
=======
def load_my_data(config, size,client_cfgs=None):
      from federatedscope.core.data import BaseDataTranslator


      transform=transforms.Compose([
        transforms.RandomRotation(10),      # rotate +/- 10 degrees
        transforms.RandomHorizontalFlip(),  # reverse 50% of images
        transforms.Resize(size), 
        transforms.CenterCrop(size),             # resize shortest side
>>>>>>> 64b283ee525ef53c32509882719e74890329b83f
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406],
                             [0.229, 0.224, 0.225])])
      data_train = ImageFolder('data/lung/train', transform=transform) 
      data_test = ImageFolder('data/lung/train', transform=transform) 
      # data_train =  DataLoader(data_train)
      # data_train =   DataLoader(data_test)
<<<<<<< HEAD

=======
      # data_train = ImageFolder('data/lung/train' ,transforms.ToTensor(),) 
      # data_test = ImageFolder('data/lung/train' ) 
>>>>>>> 64b283ee525ef53c32509882719e74890329b83f
      
      # Split data into dict
      data_dict = dict()
      data_val = data_train
      data_dict = {'train': data_train, 'val': data_val, 'test': data_test}
      data_split_tuple = (data_dict.get('train'), data_dict.get('val'),
                        data_dict.get('test'))

      translator = BaseDataTranslator(config, client_cfgs) 
<<<<<<< HEAD
      fs_data = translator([data_train,data_val, data_test])
=======
      fs_data = translator(data_train)
>>>>>>> 64b283ee525ef53c32509882719e74890329b83f
      return fs_data, config



def call_my_data(config, client_cfgs):
<<<<<<< HEAD
     if config.data.type == "lung":
         data, modified_config = load_my_data(config, client_cfgs)
         return data, modified_config

=======
     if config.data.type == "lung224":
         data, modified_config = load_my_data(config, 224,client_cfgs)
         return data, modified_config
     elif config.data.type == "lung100":
         data, modified_config = load_my_data(config, 100,client_cfgs)
         return data, modified_config
     elif config.data.type == "lung384":
         data, modified_config = load_my_data(config, 384,client_cfgs)
         return data, modified_config
     elif config.data.type == "lung":
         data, modified_config = load_my_data(config, 100,client_cfgs)
         return data, modified_config
>>>>>>> 64b283ee525ef53c32509882719e74890329b83f
register_data("lung", call_my_data)


