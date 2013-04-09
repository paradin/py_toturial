#!/usr/bin/env python
# -*- coding=utf-8 -*-
import os, sys, time

boats_routine = {1:[(10,10),(20,25),(30,30),(40,50),(50,70),(60,90),(65,100)],2:[(10,5),(20,10),(30,20),(40,40),(50,60),(60,80),(70,100)],3:[(10,10),(20,20),(30,30),(40,40),(50,50),(60,60),(70,70)],4:[(10,10),(20,25),(30,35),(40,55),(50,70),(60,80),(75,100)],5:[(10,10),(20,35),(30,40),(40,50),(50,70),(60,90),(75,90)]}

spf = 0.5
frames = 1000
boat_count = 5
race_length = 100
  
def boat_pos(idx, tm):
  assert 1 <= idx < boat_count+1 
  routine = boats_routine[idx]
  segs = boats_routine[idx]
  seg_count = len(segs)

  pos = 0
  seg_pos = 0
  for seg_pos in range(seg_count):
    pair = routine[seg_pos] 
    if pair[0] <= tm :
      pos += pair[1]
    elif seg_pos == 0:
      pos += float(pair[1])/pair[0] * tm     
      return pos
    else:
      pre_pair = routine[seg_pos-1]
      pos += float(pair[1]-pre_pair[1])/(pair[0]-pre_pair[0])*(tm-pre_pair[0]) 
      break
      
  if seg_pos == seg_count:
    end_seg = routine[seg_pos-1]
    if tm > end_seg[0]:
      not_last_end_seg = routine[seg_pos-2]
      pos += float(end_seg[1]-not_last_end_seg[1])/(end_seg[0]-not_last_end_seg[0])*(tm-not_last_end_seg[0])
  return pos

    

if __name__ == '__main__':
  for i in range(1,frames):
    os.system('cls' if os.name=='nt' else 'clear')
    sys.stdout.write(str(i)+'\n\r')

    finish = 1 
    res_dis = {} 

    for j in range(1,boat_count+1):
      dis = boat_pos(j, float(i)*spf)
      res_dis[j] = dis 
      if dis<race_length: finish = 0 

    for j in range(1,boat_count+1):
      dis = res_dis[j]
      sys.stdout.write(str(int(dis)) + '#'*int(dis) + '->' + str(j) + '\n\r')

    sys.stdout.flush()

    if finish==1: break

    time.sleep(spf)
  
    
