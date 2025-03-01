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


class NodeTrainerTest(unittest.TestCase):
    def setUp(self):
        print(('Testing %s.%s' % (type(self).__name__, self._testMethodName)))

    def set_config_node(self, cfg):
        backup_cfg = cfg.clone()

        import torch
        cfg.use_gpu = torch.cuda.is_available()
        cfg.eval.freq = 10
        cfg.eval.metrics = ['acc', 'correct']

        cfg.federate.mode = 'standalone'
        cfg.federate.total_round_num = 50
        cfg.federate.client_num = 5

        cfg.data.root = 'test_data/'
        cfg.data.type = 'cora'
        cfg.data.splitter = 'louvain'

        cfg.dataloader.type = 'pyg'
        cfg.dataloader.batch_size = 1  # full batch train

        cfg.model.type = 'gcn'
        cfg.model.hidden = 64
        cfg.model.dropout = 0.5
        cfg.model.out_channels = 7

        cfg.train.optimizer.lr = 0.25
        cfg.train.optimizer.weight_decay = 0.0005
        cfg.train.optimizer.type = 'SGD'

        cfg.criterion.type = 'CrossEntropyLoss'
        cfg.trainer.type = 'nodefullbatch_trainer'

        return backup_cfg

    def test_node_standalone(self):
        init_cfg = global_cfg.clone()
        backup_cfg = self.set_config_node(init_cfg)
        setup_seed(init_cfg.seed)
        update_logger(init_cfg, True)

        data, modified_cfg = get_data(init_cfg.clone())
        init_cfg.merge_from_other_cfg(modified_cfg)

        self.assertIsNotNone(data)

        Fed_runner = get_runner(data=data,
                                server_class=get_server_cls(init_cfg),
                                client_class=get_client_cls(init_cfg),
                                config=init_cfg.clone())
        self.assertIsNotNone(Fed_runner)
        test_best_results = Fed_runner.run()
        init_cfg.merge_from_other_cfg(backup_cfg)
        self.assertGreater(
            test_best_results["client_summarized_weighted_avg"]['test_acc'],
            0.7)


if __name__ == '__main__':
    unittest.main()
