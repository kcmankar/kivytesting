#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 19:00:23 2018

@author: kanishka
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ListProperty,ObjectProperty
from kivy.clock import Clock
from kivy.core.window import Window
class Root(Widget):
	def __init__(self,**kwargs):
		super(Root,self).__init__(**kwargs)
		Clock.schedule_interval(self.check,1/60.)
		
	def check(self,Ell):
	     ball = ObjectProperty(None)
	     rect = ObjectProperty(None)
	     if self.ball.center==self.rect.center:
	    	 self.ball.velocity[0] *= -1
	    	 self.ball.velocity[1] *= -1

	
class Move(Widget):
    def __init__(self, **kwargs):
        super(Move, self).__init__(**kwargs)
        
    def update(self , *args):
        self.x += self.velocity[0]
        self.y += self.velocity[1]

        if self.x < 0 or (self.x + self.width) > Window.width:
            
            self.velocity[0] *= -1
        if self.y < 0 or (self.y + self.height) > Window.height:
            self.velocity[1] *= -1
	   
class Ell(Move):
    velocity = ListProperty([5,5])
    def __init__(self,**kwargs):
    	super(Ell,self).__init__(**kwargs)
    	Clock.schedule_interval(self.update,1/60.)
    	
   
            
    
class Test(Move):
	velocity = ListProperty([5,5])
	def __init__(self,**kwargs):
		super(Test,self).__init__(**kwargs)
		Clock.schedule_interval(self.update,1/60.)
	
class RecApp(App):
    def build(self):
        r=Root()
        
        return r
if __name__=="__main__":
     RecApp().run()
