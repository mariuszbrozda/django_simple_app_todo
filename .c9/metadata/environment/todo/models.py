{"filter":false,"title":"models.py","tooltip":"/todo/models.py","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":3,"column":0},"end":{"row":10,"column":24},"action":"insert","lines":["# Create your models here.","class Item(models.Model):","    ","    name = models.CharField(max_length=30, blank=False)","    done = models.BooleanField(blank=False, default=False)","","    def __str__(self):","        return self.name"],"id":2}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":26},"action":"remove","lines":["# Create your models here."],"id":3}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":2,"column":0},"end":{"row":2,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1563826935353,"hash":"a28d1200718b1eb0b5d748b05113862100656709"}