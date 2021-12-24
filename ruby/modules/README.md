# Introductions to Modules
Modules are a crucial component of code organisation in Ruby. However, they can be a little confusing, so it is worth introducing them very briefly to remove any anxiety.

A module can be used simply for namespacing (e.g. certain classes or methods are contained within that module). It can then be referenced in the form `ModuleName::ModuleClass`. We have an example of this in the `Utilities` module. This is used to 'contain' the `Formatter` class, which offers a class method, `pretty_print`. This method can then be referenced by an object which has access to the module (in this case an instance of the `Test` class).

You can test this by executing the test file:
```shell
ruby test.rb
```


Another common approach is for modules to contain methods that are then provided to objects that 'include' them. This can be confusing, as we see objects reference methods that they do not define. The key thing to look for then is `include ModuleName` in the class that includes the module. We give an example of this in the `test_include.rb` file, which `includes` the `UtilitiesWithInclude` module. This allows it to use the `pretty_print` method directly without reference to a containing class or module.

You can test this by executing the test file:
```shell
ruby test_include.rb
```
