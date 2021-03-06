
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocANDORnonassocEQUALNOTEQUALnonassocLESSLESSEQUALGREATERGREATEREQUALleftPLUSMINUSleftTIMESDIVIDErightUMINUSNOTAND ASSIGN COMMA DIVIDE DO ELSE END EQUAL FOR GREATER GREATEREQUAL ID IF IN LESS LESSEQUAL LPAREN MINUS NOT NOTEQUAL NUMBER OR PLUS RPAREN SEMICOLON STRING THEN TIMES VAR WHILEblock : blocklistblocklist : empty\n                 | blocklist command blockterminatorblockterminator : empty\n                       | SEMICOLONcommand : ID ASSIGN exp\n               | functioncall\n               | vardeclaration\n               | WHILE exp DO block END\n               | IF exp THEN block elsestnt ENDelsestnt : empty\n                | ELSE blockexp : NUMBER\n           | ID\n           | functioncall\n           | exp PLUS exp\n           | exp MINUS exp\n           | exp TIMES exp\n           | exp DIVIDE exp\n           | exp LESS exp\n           | exp LESSEQUAL exp\n           | exp GREATER exp\n           | exp GREATEREQUAL exp\n           | exp EQUAL exp\n           | exp NOTEQUAL exp\n           | exp AND exp\n           | exp OR exp\n           | NOT exp\n           | MINUS exp %prec UMINUS\n           | LPAREN exp RPARENfunctioncall : ID LPAREN explist RPARENvardeclaration : VAR ID expassignexpassign : empty\n                 | ASSIGN expexplist : empty\n               | lexp explexp : empty\n            | lexp exp COMMAempty : '
    
_lr_action_items = {'ID':([0,2,3,4,6,7,8,9,10,11,12,13,14,15,17,18,19,20,21,22,24,25,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,46,47,48,49,52,53,54,55,56,57,58,59,60,61,62,63,64,66,67,68,71,72,],[-39,5,-2,-39,-7,-8,18,18,24,-3,-4,-5,18,-39,-13,-14,-15,18,18,18,-39,-6,-37,18,-39,18,18,18,18,18,18,18,18,18,18,18,18,-29,-28,-39,-32,-33,18,-31,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-30,-34,-38,-9,-39,-10,]),'WHILE':([0,2,3,4,6,7,11,12,13,17,18,19,24,25,29,42,43,45,46,47,49,52,53,54,55,56,57,58,59,60,61,62,63,64,66,68,71,72,],[-39,8,-2,-39,-7,-8,-3,-4,-5,-13,-14,-15,-39,-6,-39,-29,-28,-39,-32,-33,-31,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-30,-34,-9,-39,-10,]),'IF':([0,2,3,4,6,7,11,12,13,17,18,19,24,25,29,42,43,45,46,47,49,52,53,54,55,56,57,58,59,60,61,62,63,64,66,68,71,72,],[-39,9,-2,-39,-7,-8,-3,-4,-5,-13,-14,-15,-39,-6,-39,-29,-28,-39,-32,-33,-31,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-30,-34,-9,-39,-10,]),'VAR':([0,2,3,4,6,7,11,12,13,17,18,19,24,25,29,42,43,45,46,47,49,52,53,54,55,56,57,58,59,60,61,62,63,64,66,68,71,72,],[-39,10,-2,-39,-7,-8,-3,-4,-5,-13,-14,-15,-39,-6,-39,-29,-28,-39,-32,-33,-31,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-30,-34,-9,-39,-10,]),'$end':([0,1,2,3,4,6,7,11,12,13,17,18,19,24,25,42,43,46,47,49,52,53,54,55,56,57,58,59,60,61,62,63,64,66,68,72,],[-39,0,-1,-2,-39,-7,-8,-3,-4,-5,-13,-14,-15,-39,-6,-29,-28,-32,-33,-31,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-30,-34,-9,-10,]),'END':([2,3,4,6,7,11,12,13,17,18,19,24,25,29,42,43,45,46,47,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,70,71,72,73,],[-1,-2,-39,-7,-8,-3,-4,-5,-13,-14,-15,-39,-6,-39,-29,-28,-39,-32,-33,-31,68,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-30,-39,-34,-9,72,-11,-39,-10,-12,]),'ELSE':([2,3,4,6,7,11,12,13,17,18,19,24,25,42,43,45,46,47,49,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,72,],[-1,-2,-39,-7,-8,-3,-4,-5,-13,-14,-15,-39,-6,-29,-28,-39,-32,-33,-31,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-30,71,-34,-9,-10,]),'SEMICOLON':([4,6,7,17,18,19,24,25,42,43,46,47,49,52,53,54,55,56,57,58,59,60,61,62,63,64,66,68,72,],[13,-7,-8,-13,-14,-15,-39,-6,-29,-28,-32,-33,-31,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-30,-34,-9,-10,]),'ASSIGN':([5,24,],[14,48,]),'LPAREN':([5,8,9,14,15,18,20,21,22,27,28,30,31,32,33,34,35,36,37,38,39,40,41,48,67,],[15,22,22,22,-39,15,22,22,22,-37,22,22,22,22,22,22,22,22,22,22,22,22,22,22,-38,]),'NUMBER':([8,9,14,15,20,21,22,27,28,30,31,32,33,34,35,36,37,38,39,40,41,48,67,],[17,17,17,-39,17,17,17,-37,17,17,17,17,17,17,17,17,17,17,17,17,17,17,-38,]),'NOT':([8,9,14,15,20,21,22,27,28,30,31,32,33,34,35,36,37,38,39,40,41,48,67,],[21,21,21,-39,21,21,21,-37,21,21,21,21,21,21,21,21,21,21,21,21,21,21,-38,]),'MINUS':([8,9,14,15,16,17,18,19,20,21,22,23,25,27,28,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,48,49,50,52,53,54,55,56,57,58,59,60,61,62,63,64,66,67,],[20,20,20,-39,31,-13,-14,-15,20,20,20,31,31,-37,20,20,20,20,20,20,20,20,20,20,20,20,20,-29,-28,31,20,-31,31,-16,-17,-18,-19,31,31,31,31,31,31,31,31,-30,31,-38,]),'RPAREN':([15,17,18,19,26,27,42,43,44,49,50,52,53,54,55,56,57,58,59,60,61,62,63,64,],[-39,-13,-14,-15,49,-35,-29,-28,64,-31,-36,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-30,]),'DO':([16,17,18,19,42,43,49,52,53,54,55,56,57,58,59,60,61,62,63,64,],[29,-13,-14,-15,-29,-28,-31,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-30,]),'PLUS':([16,17,18,19,23,25,42,43,44,49,50,52,53,54,55,56,57,58,59,60,61,62,63,64,66,],[30,-13,-14,-15,30,30,-29,-28,30,-31,30,-16,-17,-18,-19,30,30,30,30,30,30,30,30,-30,30,]),'TIMES':([16,17,18,19,23,25,42,43,44,49,50,52,53,54,55,56,57,58,59,60,61,62,63,64,66,],[32,-13,-14,-15,32,32,-29,-28,32,-31,32,32,32,-18,-19,32,32,32,32,32,32,32,32,-30,32,]),'DIVIDE':([16,17,18,19,23,25,42,43,44,49,50,52,53,54,55,56,57,58,59,60,61,62,63,64,66,],[33,-13,-14,-15,33,33,-29,-28,33,-31,33,33,33,-18,-19,33,33,33,33,33,33,33,33,-30,33,]),'LESS':([16,17,18,19,23,25,42,43,44,49,50,52,53,54,55,56,57,58,59,60,61,62,63,64,66,],[34,-13,-14,-15,34,34,-29,-28,34,-31,34,-16,-17,-18,-19,None,None,None,None,34,34,34,34,-30,34,]),'LESSEQUAL':([16,17,18,19,23,25,42,43,44,49,50,52,53,54,55,56,57,58,59,60,61,62,63,64,66,],[35,-13,-14,-15,35,35,-29,-28,35,-31,35,-16,-17,-18,-19,None,None,None,None,35,35,35,35,-30,35,]),'GREATER':([16,17,18,19,23,25,42,43,44,49,50,52,53,54,55,56,57,58,59,60,61,62,63,64,66,],[36,-13,-14,-15,36,36,-29,-28,36,-31,36,-16,-17,-18,-19,None,None,None,None,36,36,36,36,-30,36,]),'GREATEREQUAL':([16,17,18,19,23,25,42,43,44,49,50,52,53,54,55,56,57,58,59,60,61,62,63,64,66,],[37,-13,-14,-15,37,37,-29,-28,37,-31,37,-16,-17,-18,-19,None,None,None,None,37,37,37,37,-30,37,]),'EQUAL':([16,17,18,19,23,25,42,43,44,49,50,52,53,54,55,56,57,58,59,60,61,62,63,64,66,],[38,-13,-14,-15,38,38,-29,-28,38,-31,38,-16,-17,-18,-19,-20,-21,-22,-23,None,None,38,38,-30,38,]),'NOTEQUAL':([16,17,18,19,23,25,42,43,44,49,50,52,53,54,55,56,57,58,59,60,61,62,63,64,66,],[39,-13,-14,-15,39,39,-29,-28,39,-31,39,-16,-17,-18,-19,-20,-21,-22,-23,None,None,39,39,-30,39,]),'AND':([16,17,18,19,23,25,42,43,44,49,50,52,53,54,55,56,57,58,59,60,61,62,63,64,66,],[40,-13,-14,-15,40,40,-29,-28,40,-31,40,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,None,None,-30,40,]),'OR':([16,17,18,19,23,25,42,43,44,49,50,52,53,54,55,56,57,58,59,60,61,62,63,64,66,],[41,-13,-14,-15,41,41,-29,-28,41,-31,41,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,None,None,-30,41,]),'THEN':([17,18,19,23,42,43,49,52,53,54,55,56,57,58,59,60,61,62,63,64,],[-13,-14,-15,45,-29,-28,-31,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-30,]),'COMMA':([17,18,19,42,43,49,50,52,53,54,55,56,57,58,59,60,61,62,63,64,],[-13,-14,-15,-29,-28,-31,67,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-30,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'block':([0,29,45,71,],[1,51,65,73,]),'blocklist':([0,29,45,71,],[2,2,2,2,]),'empty':([0,4,15,24,29,45,65,71,],[3,12,27,47,3,3,70,3,]),'command':([2,],[4,]),'functioncall':([2,8,9,14,20,21,22,28,30,31,32,33,34,35,36,37,38,39,40,41,48,],[6,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'vardeclaration':([2,],[7,]),'blockterminator':([4,],[11,]),'exp':([8,9,14,20,21,22,28,30,31,32,33,34,35,36,37,38,39,40,41,48,],[16,23,25,42,43,44,50,52,53,54,55,56,57,58,59,60,61,62,63,66,]),'explist':([15,],[26,]),'lexp':([15,],[28,]),'expassign':([24,],[46,]),'elsestnt':([65,],[69,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> block","S'",1,None,None,None),
  ('block -> blocklist','block',1,'p_block','parser.py',18),
  ('blocklist -> empty','blocklist',1,'p_blocklist','parser.py',22),
  ('blocklist -> blocklist command blockterminator','blocklist',3,'p_blocklist','parser.py',23),
  ('blockterminator -> empty','blockterminator',1,'p_blockterminator','parser.py',30),
  ('blockterminator -> SEMICOLON','blockterminator',1,'p_blockterminator','parser.py',31),
  ('command -> ID ASSIGN exp','command',3,'p_command','parser.py',35),
  ('command -> functioncall','command',1,'p_command','parser.py',36),
  ('command -> vardeclaration','command',1,'p_command','parser.py',37),
  ('command -> WHILE exp DO block END','command',5,'p_command','parser.py',38),
  ('command -> IF exp THEN block elsestnt END','command',6,'p_command','parser.py',39),
  ('elsestnt -> empty','elsestnt',1,'p_elsestnt','parser.py',50),
  ('elsestnt -> ELSE block','elsestnt',2,'p_elsestnt','parser.py',51),
  ('exp -> NUMBER','exp',1,'p_exp','parser.py',58),
  ('exp -> ID','exp',1,'p_exp','parser.py',59),
  ('exp -> functioncall','exp',1,'p_exp','parser.py',60),
  ('exp -> exp PLUS exp','exp',3,'p_exp','parser.py',61),
  ('exp -> exp MINUS exp','exp',3,'p_exp','parser.py',62),
  ('exp -> exp TIMES exp','exp',3,'p_exp','parser.py',63),
  ('exp -> exp DIVIDE exp','exp',3,'p_exp','parser.py',64),
  ('exp -> exp LESS exp','exp',3,'p_exp','parser.py',65),
  ('exp -> exp LESSEQUAL exp','exp',3,'p_exp','parser.py',66),
  ('exp -> exp GREATER exp','exp',3,'p_exp','parser.py',67),
  ('exp -> exp GREATEREQUAL exp','exp',3,'p_exp','parser.py',68),
  ('exp -> exp EQUAL exp','exp',3,'p_exp','parser.py',69),
  ('exp -> exp NOTEQUAL exp','exp',3,'p_exp','parser.py',70),
  ('exp -> exp AND exp','exp',3,'p_exp','parser.py',71),
  ('exp -> exp OR exp','exp',3,'p_exp','parser.py',72),
  ('exp -> NOT exp','exp',2,'p_exp','parser.py',73),
  ('exp -> MINUS exp','exp',2,'p_exp','parser.py',74),
  ('exp -> LPAREN exp RPAREN','exp',3,'p_exp','parser.py',75),
  ('functioncall -> ID LPAREN explist RPAREN','functioncall',4,'p_functioncall','parser.py',90),
  ('vardeclaration -> VAR ID expassign','vardeclaration',3,'p_vardeclaration','parser.py',94),
  ('expassign -> empty','expassign',1,'p_expassign','parser.py',98),
  ('expassign -> ASSIGN exp','expassign',2,'p_expassign','parser.py',99),
  ('explist -> empty','explist',1,'p_explist','parser.py',106),
  ('explist -> lexp exp','explist',2,'p_explist','parser.py',107),
  ('lexp -> empty','lexp',1,'p_lexp','parser.py',114),
  ('lexp -> lexp exp COMMA','lexp',3,'p_lexp','parser.py',115),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',122),
]
