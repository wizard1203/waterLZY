from pprint import pprint
from pprint import pformat

    nets = ['waternetsmallfl', 'watercnndsnetf_in4_out58', 'waterdsnetf_in4_out58', 'waterdsnetf_self_define']

    # pretrained

    # weight_decay['waternetsmallfl'] = 0.00005
    # lr_decay['waternetsmallfl'] = 0.33

    # lr['watercnndsnetf_in4_out58'] = 0.1
    # weight_decay['watercnndsnetf_in4_out58'] = 0.00005
    # lr_decay['watercnndsnetf_in4_out58'] = 0.33

    # lr['waterdsnetf_in4_out58'] = 0.2
    # weight_decay['waterdsnetf_in4_out58'] = 0.00005
    # lr_decay['waterdsnetf_in4_out58'] = 0.33

    activation = 'relu'

    lr = 0.6
    weight_decay = 0.00005
    lr_decay = 0.33  #

    # record i-th log
    kind = '0'

    # set gpu :
    # gpu = True

    # visualization
    env = 'water-nn'  # visdom env
    port = 8097
    plot_every = 40  # vis every N iter

    # preset
    data = 'water'

    # training
    epoch = 120

    load_path = None
    save_path = '~/water/modelparams'

    # len(labels_dict) == 12
    labels_dict_12 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
    )

    # len(labels_dict) == 58
    labels_dict_58 = (379, 385, 390, 391, 392, 406, 414, 415, 416, 417, 418, 419, 420, 422,
    425, 434, 435, 436, 438, 439, 440, 441, 443, 444, 445, 446, 447, 448, 449,
    450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 464, 465, 466, 468, 512,
    513, 514, 515, 517, 518, 519, 520, 557, 558, 559, 560, 561, 562
    )
    labels_dict = ()

    def _parse(self, kwargs):
        state_dict = self._state_dict()
        for k, v in kwargs.items():
            if k not in state_dict:
                raise ValueError('UnKnown Option: "--%s"' % k)
            setattr(self, k, v)

        print('======user config========')
        pprint(self._state_dict())
        print('==========end============')
        if opt.customize:
            logging_name = 'log' + '_self_' + opt.arch + '_'+ opt.optim + opt.kind + '_lr_' + str(self.lr) + '.txt' 
        else:
            logging_name = 'log' + '_default_' + opt.arch  + '_' + opt.optim + opt.kind + '_lr_' + str(self.lr) + '.txt'
        if not os.path.exists('log'):
            os.mkdir('log')

        if opt.arch == 'waterdsnetf':
            self.labels_dict = self.labels_dict_12
        elif opt.arch == 'waterdsnetf_in4_out58':
            self.labels_dict = self.labels_dict_58
        elif opt.arch == 'waterdsnetf_self_define':
            self.labels_dict = self.labels_dict_12
        elif opt.arch == 'watercnndsnetf_in4_out58':
            self.labels_dict = self.labels_dict_58
        elif opt.arch == 'waternetsmallfl':
            self.labels_dict = self.labels_dict_58

        logging_path = os.path.join('log', logging_name) 
    
        logging.basicConfig(level=logging.DEBUG,
                        filename=logging_path,
                        filemode='a',
                        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                        datefmt='%H:%M:%S')
        logging.info('Logging for {}'.format(opt.arch))
        logging.info('======user config========')
        logging.info(pformat(self._state_dict()))
        logging.info('==========end============')
        # logging.info('optim : [{}], batch_size = {}, lr = {}, weight_decay= {}, momentum = {}'.format( \
        #                 args.optim, args.batch_size,
        #                 args.lr, args.weight_decay, args.momentum) )


    def _state_dict(self):
        return {k: getattr(self, k) for k, _ in Config.__dict__.items() \
                if not k.startswith('_')}
    

opt = Config()
