import constants

class PlayRset(object):
    """游戏分数记录"""
    _score = 0 # 总分
    _life = 3 # 生命数量
    _blood = 1000 # 生命值

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if value < 0 :
            pass
        else:
            self._score = value

    def set_history(self):
        """记录历史最高分"""
        if int(self.get_max_core()) < self.score :
            with open(constants.PLAY_RESULT_FILE, 'w') as f:
                f.write('{}'.format(self.score))


    def get_max_core(self):
        '''读取文件中的历史最高分'''
        with open(constants.PLAY_RESULT_FILE, 'r') as f:
            rest = f.read()
            if rest :
                return rest
            else:
                return -1