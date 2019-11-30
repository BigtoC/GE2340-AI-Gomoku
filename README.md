# GE2340-AI-Gomoku
Group Project for [GE2340](https://www.cityu.edu.hk/catalogue/ug/current/course/GE2340.htm) &lt;AI:Past, Present, and Future>, play Gomoku online 
  
1. Reproduce existing methods of AlphaZero.
2. Play online matches using AlphaZero (Here's the [match website](https://dkmgames.com/Gomoku/gomoku.htm))  

---
  
## AlphaZero
#### Train Model using existing AlphaZero Algorithm  
  
## Online-Match
#### Controls the browser to auto match online using [Pyppeteer](https://github.com/miyakogi/pyppeteer)
1. **main**
   1. global control and run all modules
2. **get_chessboard**
   1. visit the website and get source codes
   2. locate the position of the chessboard
   3. download chessboard pictures as records for every step 
3. **move_chess**
   1. return opponent movement
   2. receive signal from 2 send to AlphaZero
   3. receive command from AlphaZero
   4. move corresponding chess
4. **monitor_result**
   1. check if is my turn
   2. monitor from source code and judge the result
   3. print console message with time
   4. function help the program randomly wait some time
5. **global_data**
   1. store data
   2. store user's input
  
  
 
