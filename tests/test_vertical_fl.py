# Copyright (c) Alibaba, Inc. and its affiliates.
import unittest

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 64b283ee525ef53c32509882719e74890329b83f
from medscale.core.auxiliaries.data_builder import get_data
from medscale.core.auxiliaries.worker_builder import get_client_cls, get_server_cls
from medscale.core.auxiliaries.utils import setup_seed
from medscale.core.auxiliaries.logging import update_logger
from medscale.core.configs.config import global_cfg
from medscale.core.auxiliaries.runner_builder import get_runner
<<<<<<< HEAD
=======
=======
from medscale.core.auxiliaries.data_builder import get_data
from medscale.core.auxiliaries.worker_builder import get_client_cls, get_server_cls
from medscale.core.auxiliaries.utils import setup_seed
from medscale.core.auxiliaries.logging import update_logger
from medscale.core.configs.config import global_cfg
from medscale.core.auxiliaries.runner_builder import get_runner
>>>>>>> fe4962455354c9c11afd9c9806ceda28eb280737
>>>>>>> 64b283ee525ef53c32509882719e74890329b83f


class vFLTest(unittest.TestCase):
    def setUp(self):
        print(('Testing %s.%s' % (type(self).__name__, self._testMethodName)))

    def set_config(self, cfg):
        backup_cfg = cfg.clone()

        import torch
        cfg.use_gpu = torch.cuda.is_available()

        cfg.federate.mode = 'standalone'
        cfg.federate.total_round_num = 30
        cfg.federate.client_num = 2

        cfg.model.type = 'lr'
        cfg.model.use_bias = False

        cfg.train.optimizer.lr = 0.05

        cfg.data.type = 'synthetic_vfl_data'
        cfg.data.size = 50

        cfg.dataloader.type = 'raw'

        cfg.vertical.use = True
        cfg.vertical.key_size = 256

        cfg.trainer.type = 'none'
        cfg.eval.freq = 5
        cfg.eval.best_res_update_round_wise_key = "test_loss"

        return backup_cfg

    def test_vFL(self):
        init_cfg = global_cfg.clone()
        backup_cfg = self.set_config(init_cfg)
        setup_seed(init_cfg.seed)
        update_logger(init_cfg, True)

        data, modified_config = get_data(init_cfg.clone())
        init_cfg.merge_from_other_cfg(modified_config)
        self.assertIsNotNone(data)

        Fed_runner = get_runner(data=data,
                                server_class=get_server_cls(init_cfg),
                                client_class=get_client_cls(init_cfg),
                                config=init_cfg.clone())
        self.assertIsNotNone(Fed_runner)
        test_results = Fed_runner.run()
        init_cfg.merge_from_other_cfg(backup_cfg)
        print(test_results)
        self.assertGreater(test_results['server_global_eval']['test_acc'], 0.8)


if __name__ == '__main__':
    unittest.main()
