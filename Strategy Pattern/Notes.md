Here initially we tried to use inheritance and make methods in Duck superclass and try to use the same in subclass.
But we started to get problems as those duck which cann't fly now are able to fly. So to handle this thing we have overridden this function in particular duck class. But there could be 1000 class where they need to do change and if they have to do it frequently then it's a nightmare for developers.

Let's try Interface
Now we will take the fly and quack code out in interface and only those duckw whoc can fly or quack will use these interfaces. So suppose out of 1000, 300 ducks subclasses uses these interfaces so we need to implement it at 300 places. Again these is no role of code reusability here.
