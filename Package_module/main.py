# animal package
# dog, cat modules
# dog, cat modules can say "hi"

#패키지는 모듈의 합

from animal import dog #animal 패키지에서 dog라는 모듈을 가져와줘
from animal import cat #animal 패키지에서 cat라는 모듈을 가져와줘

from animal import * #animal 패키지가 갖고 있는 모듈을 다 불러와

d=dog.Dog() #instance
c=cat.Cat()

d.hi()
c.hi()
