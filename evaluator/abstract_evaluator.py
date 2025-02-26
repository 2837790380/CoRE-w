class AbstractEvaluator(object):

    def __init__(self, config, data_feature):
        raise NotImplementedError('evaluator not implemented')

    def collect(self, batch):
        raise NotImplementedError('evaluator collect not implemented')

    def evaluate(self, best_epoch):
        raise NotImplementedError('evaluator evaluate not implemented')

    def save_result(self, save_path, filename=None):
        raise NotImplementedError('evaluator save_result not implemented')

    def clear(self):
        raise NotImplementedError('evaluator clear not implemented')
