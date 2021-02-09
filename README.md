# Building Android Apps With Python

# [University of Glasgow - Glasgow International College](www.glasgow.ac.uk/gic) 
## [GIC PM-617 Module: Practical Training for Science and Engineering Research](https://pathways.kaplaninternational.com/course/view.php?id=2879)

This is a repository for materials used for a module on quantitative research resources, taught at Glasgow International College at The University of Glasgow. 

<p align="justify">

## Intro 

The Android universe is mainly build using Java and Kotlin, but in recent times, Python has made its way into every domain and Android is no different. In this series of articles, we will look at how to set-up the required environment, the basics of developing an Android app, referencing the documentation, and how to get started with your own projects.

</p>

<p align="justify">

Android development in Python has been made possible thanks to an open-source Python library for developing mobile apps and other multi-touch application software called [Kivy](https://github.com/kivy/kivy), first released in 2011. Kivy not only supports Android applications development but also Ios, Linux, macOS X, and Windows. It is written in Python and Cython, and most of the core developers are from Russia.

We will use Kivy a lot for the front-end of the application and also [KivyMD](https://github.com/kivymd/KivyMD), a collection of Material Design compliant widgets for use with Kivy.
</p>

## How to use

1. You will need to install and setup Python. To install and setup for Mac and Windows, [you can follow this tutorial.](https://www.youtube.com/watch?v=YYXdXT2l-Gg&t=0s).

2. Download this repo as a zip file and unzip it.

3. To open the folder with the tutorial, you will need an IDE (Integrated Development Environment). There are many popular IDE environments for Python development. I use Visual Studio Code. If you use Windows, you can follow the instructions on how to install VS Code in your laptop or PC [on this link.](https://www.youtube.com/watch?v=-nh9rCzPJ20). Or if you use a Mac, [you can follow this link instead.](https://www.youtube.com/watch?v=06I63_p-2A4).

4. It’s usually a good practice to set-up a new environment for new projects as it helps in maintaining the different versions of different libraries. It also in isolating custom codes and makes it easier while deploying your application on any platform. I use a virtual environment for creating and managing my environments. You can use any other package manager but to follow along with me, you can use the same environemnt. I will name my environment `app`[See this guide to set up your virtual environment too.](https://realpython.com/python-virtual-environments-a-primer/).

```
python -m venv app
app\Scripts\activate
```

5. We are ready to install the required libraries. As we are using python, `pip` is a great way to install and manage python packages. To install Kivy and its dependencies, type the following command one-by-one in your terminal:

```
pip install kivy
pip install kivy-deps.angle
pip install kivy-deps.glew
pip install kivy-deps.gstreamer
pip install kivy-deps.sdl2
pip install kivymd

```

Then create the `requirements.txt` by running this command: 

```
pip freeze -l > requirements.txt 
```

4. Follow the step by step and let’s code!

Before we start, we need to understand some points here:

- An android app has a front-end (UI/UX) or the interactive part where the user interacts with your application and all the inputs are given via this layer.

- The inputs are transferred to the backend layer, which is our python code. This backend layer controls the flow, processes the outputs, and the content to be displayed on the screen.
Here, Object-Oriented Programming is highly used and most of the programming will be done using this concept so if you are lacking in this then I would suggest you follow this awesome tutorial on [Python Object Oriented Programming (OOP)](https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc)

5. In the WORKSHOP-LESSON folder, you can find the lessons where we go step by step to build your own android app, as shown in the live session.  

6. E-portfolio Evidence: Just focus on finishing the step-by-step and running your app in your local setup. Then, write a short 500-1000 word reflection on the course, what you learned, if you managed to run your app, how was it, if you didn’t, why? And this, accompanied by screenshots of your local setup with the app. 



<br><br>

#### Course Instructor: [Graciela Carrillo](mailto:graciela.carrillo@kaplan.com?subject=[Build-your-own-app]%20Source%20Han%20Sans)
#### Module Coordinator: [Dr. Molly Huq](mailto:graciela.carrillo@kaplan.com?subject=[Build-your-own-app]%20Source%20Han%20Sans)

<br><br>
 
## Other Resources 

[Erik Sandberg's KivyMD playlist](https://www.youtube.com/playlist?list=PLy5hjmUzdc0nMkzhphsqgPCX62NFhkell)

[buildwithpython KivyMD playlist](https://www.youtube.com/playlist?list=PLhTjy8cBISEoQQLZ9IBlVlr4WjVoStmy-)

[KivyMD docs](https://kivymd.readthedocs.io/en/latest/)

[Python Beginner Tutorial. Full playlist: 26 videos](https://www.youtube.com/watch?v=YYXdXT2l-Gg&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7)

[Learn Python - Full Course for Beginners](https://www.youtube.com/watch?v=rfscVS0vtbw)

[Intermediate Python.](https://www.youtube.com/watch?v=HGOBQPFzWKo)

[Python Object Oriented Programming (OOP). Full playlist: 6 videos](https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc)

[Git and GitHub for Beginners, Crash Course](https://www.youtube.com/watch?v=RGOj5yH7evk)
