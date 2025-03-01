# Copyright (c) Alibaba, Inc. and its affiliates.
import unittest

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 64b283ee525ef53c32509882719e74890329b83f
from medscale.core.auxiliaries.data_builder import get_data
from medscale.core.auxiliaries.utils import setup_seed
from medscale.core.auxiliaries.logging import update_logger
from medscale.core.configs.config import global_cfg
from medscale.core.auxiliaries.runner_builder import get_runner
from medscale.core.auxiliaries.worker_builder import get_server_cls, get_client_cls
<<<<<<< HEAD
=======
=======
from medscale.core.auxiliaries.data_builder import get_data
from medscale.core.auxiliaries.utils import setup_seed
from medscale.core.auxiliaries.logging import update_logger
from medscale.core.configs.config import global_cfg
from medscale.core.auxiliaries.runner_builder import get_runner
from medscale.core.auxiliaries.worker_builder import get_server_cls, get_client_cls
>>>>>>> fe4962455354c9c11afd9c9806ceda28eb280737
>>>>>>> 64b283ee525ef53c32509882719e74890329b83f


class RECTest(unittest.TestCase):
    def setUp(self):
        print(('Testing %s.%s' % (type(self).__name__, self._testMethodName)))

    def set_config_femnist(self, cfg):
        backup_cfg = cfg.clone()

        import torch
        cfg.use_gpu = torch.cuda.is_available()
        cfg.eval.freq = 10
        cfg.eval.metrics = ['acc', 'loss_regular']

        cfg.federate.mode = 'standalone'
        cfg.train.local_update_steps = 1
        cfg.federate.total_round_num = 1
        cfg.federate.sample_client_num = 1
        cfg.federate.client_num = 1

        cfg.data.root = 'test_data/'
        cfg.data.type = 'femnist'
        cfg.data.splits = [0.6, 0.2, 0.2]
        cfg.data.batch_size = 1
        cfg.data.subsample = 0.01
        cfg.data.transform = [['ToTensor'],
                              [
                                  'Normalize', {
                                      'mean': [0.1307],
                                      'std': [0.3081]
                                  }
                              ]]

        cfg.model.type = 'convnet2'
        cfg.model.hidden = 2048
        cfg.model.out_channels = 62
        cfg.model.dropout = 0

        cfg.train.optimizer.lr = 0.001
        cfg.train.optimizer.weight_decay = 0.0

        cfg.criterion.type = 'CrossEntropyLoss'
        cfg.trainer.type = 'cvtrainer'
        cfg.seed = 123

        cfg.attack.attack_method = 'dlg'
        cfg.attack.reconstruct_lr = 0.1
        cfg.attack.reconstruct_optim = 'Adam'
        cfg.attack.info_diff_type = 'l2'
        cfg.attack.max_ite = 500

        return backup_cfg

    def test_rec_femnist_standalone(self):
        init_cfg = global_cfg.clone()
        backup_cfg = self.set_config_femnist(init_cfg)
        setup_seed(init_cfg.seed)
        update_logger(init_cfg, True)

        data, modified_cfg = get_data(init_cfg.clone())
        init_cfg.merge_from_other_cfg(modified_cfg)
        self.assertIsNotNone(data)

        #         if cfg.attack.attack_method.lower() == 'dlg':
<<<<<<< HEAD
        #             from medscale.attack.worker_as_attacker.server_attacker import PassiveServer
=======
<<<<<<< HEAD
        #             from medscale.attack.worker_as_attacker.server_attacker import PassiveServer
=======
        #             from medscale.attack.worker_as_attacker.server_attacker import PassiveServer
>>>>>>> fe4962455354c9c11afd9c9806ceda28eb280737
>>>>>>> 64b283ee525ef53c32509882719e74890329b83f
        #             server_class = PassiveServer
        #         else:
        #             server_class = Server

        Fed_runner = get_runner(data=data,
                                server_class=get_server_cls(init_cfg),
                                client_class=get_client_cls(init_cfg),
                                config=init_cfg.clone())
        self.assertIsNotNone(Fed_runner)
        test_best_results = Fed_runner.run()
        print(test_best_results)
        init_cfg.merge_from_other_cfg(backup_cfg)
        self.assertLess(
            test_best_results["client_summarized_weighted_avg"]['test_loss'],
            600)
        for round in test_best_results['DLG_loss'].keys():
            for client_id in test_best_results['DLG_loss'][round].keys():
                self.assertLess(
                    test_best_results['DLG_loss'][round][client_id], 10)


if __name__ == '__main__':
    unittest.main()
