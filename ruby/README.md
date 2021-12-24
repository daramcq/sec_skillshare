# Introduction to Ruby
Here we will introduce some Ruby concepts. As there is a surplus of content online on the language, we will focus on explaining some of the important concepts for writing maintainable software in Ruby. These will be: package management (using Bundle), unit-testing (using Minitest) and modules. I will also explain some of the basics of the ActiveRecord library and recommend some steps to take to become more comfortable using this in the context of a project.

## One note on the language
Note that everything is an object. This is a bit different to languages like Python, so it's worth bearing in mind. This applies when you are performing actions like iteration. So for instance, iterating through a list and printing its items looks like the below in Python.
```python
mylist = [1, 2, 3]
[print(x) for x in mylist]
```
In Ruby, the iteration is done with the `.each` method, which takes a block of code:
```ruby
mylist = [1, 2, 3]
mylist.each { |x| puts x }
```
The `.each` method is a method on the `Array` object.

## Ruby versions
This folder includes a `.ruby-version` file. This tells your Ruby version manager which version of Ruby to use. Your RVM will probably tell you the right command, but if not, here it is:
```
rvm install "ruby-3.0.3"
```

## Using the interpreter
The built-in Ruby interpreter is `IRB`. This gives you a Ruby command-line to test code. You can access it by typing `irb` from this directory. Once you have done this, test some basic code, for instance `1+1`, `puts 'foo'` or, from the above, `[1, 2, 3].each { |x| puts x }`. 

Then, test package import with the below:
```ruby
> require 'faraday'
```
Unless you have installed this package elsewhere on your voyage of discovery, you will see an error. This is where the next step comes in.

## Package management
Package management is an important concept to cover, because it is required for working on any project of significance. We'll just look at the basics of installing a package. I have added a Gemfile to the project. Once you have installed the correct version of Ruby, please install Bundler, which is the most popular Ruby package manager. Exit from `IRB` if you are still there with `Ctrl-D` or `exit`.
```shell
gem install bundler
```
Now look at the Gemfile. You will see `'faraday'`, which is a common HTTP library for Ruby, similar to Python's Requests module. You can install this with `bundle install`. Note that a `Gemfile.lock` file has now been created. This tracks the library versions you are using. To verify that the Faraday gem has been installed, go back to your `IRB`:
```rb
> require 'faraday'
 => true
 ```
 The `true` indicates that the library is available to you and has been imported into the context of the interpreter. This means that you can use its classes and methods. For usage, please see the instructions on the gem's [documentation site](https://lostisland.github.io/faraday/usage/).
 
## Next steps
 Please see the testing subdirectory for some guidance on writing unit tests and then the modules subdirectory for information on Ruby modules and how to use them. If you have time, I would recommend seeking out an Active Record tutorial and beginning a trial project. Ideally, I would recommend installing Active Record independently of Rails, and using it as an ORM for whatever database you are most familiar with. 
 
 If you wish to put all the above components together, you could write a program that downloads data from a public API (for e.g. the [Star Wars API](https://swapi.dev/)) using Faraday, and then stores it in a database using Active Record. Unit-testing each of those components could be a useful challenge.
