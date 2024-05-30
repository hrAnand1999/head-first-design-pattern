Here initially we tried to use inheritance and make methods in Duck superclass and try to use the same in subclass.
But we started to get problems as those duck which cann't fly now are able to fly. So to handle this thing we have overridden this function in particular duck class. But there could be 1000 class where they need to do change and if they have to do it frequently then it's a nightmare for developers.

Let's try Interface
Now we will take the fly and quack code out in interface and only those duck who can fly or quack will use these interfaces. So suppose out of 1000, 300 ducks subclasses uses these interfaces so we need to implement it at 300 places. Again there is no role of code reusability here. And if we need to change any behaviour we need to modify at all places where we have implemented this function.


Let's try something new
=> Take what varies and "encapsulate" it so it won't affect the rest of your code.
The result? Fewer unintended consequences from code changes and more flexibility in your systems

Here in our code the flying behaviour varies with duck, so we will make separate class for them and use them in duck sub class. So if we have to change anything with behaviour in future we will only need to change at one place instead of all duck sub classes where we have used it.
