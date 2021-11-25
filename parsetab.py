
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEATTRIB COMMA DIVIDE DOUBLEEQUALS FUNC ID IF LBR LPAREN LT LTE MINUS NE NUMBER PLUS RBR RETURN RPAREN RT RTE SEMICOLON TIMES WHILEfunctions : function functions\n                | empty\n    function : FUNC ID LPAREN params RPAREN LBR statements RBRpcall : logic pclist\n             | empty\n     pclist : COMMA logic pclist\n             | empty\n    params : ID plist\n              | empty\n     plist : COMMA ID plist\n             | empty\n    statements : statement statements\n                | empty\n    statement : attrib\n                | if\n                | while\n                | return\n                empty : if : IF LPAREN logic RPAREN LBR statements RBRwhile : WHILE LPAREN logic RPAREN LBR statements RBRreturn : RETURN logic SEMICOLONattrib : ID ATTRIB logic SEMICOLONlogic : logic LT logiclogic : logic RT logiclogic : logic LTE logiclogic : logic RTE logiclogic : logic DOUBLEEQUALS logiclogic : logic NE logiclogic : expressionexpression : expression PLUS expressionexpression : expression MINUS expressionexpression : termterm : term TIMES termterm : term DIVIDE termterm : callterm : NUMBERterm : IDcall : ID LPAREN pcall RPAREN term : LPAREN expression RPAREN'
    
_lr_action_items = {'FUNC':([0,2,30,],[4,4,-3,]),'$end':([0,1,2,3,5,30,],[-18,0,-18,-2,-1,-3,]),'ID':([4,7,12,16,20,22,23,24,25,28,29,32,33,40,44,45,46,47,48,49,50,51,52,53,54,55,57,74,75,78,83,84,],[6,8,15,18,18,-14,-15,-16,-17,39,39,39,39,39,-21,39,39,39,39,39,39,39,39,39,39,39,-22,18,18,39,-19,-20,]),'LPAREN':([6,26,27,28,29,32,33,39,40,45,46,47,48,49,50,51,52,53,54,55,78,],[7,32,33,40,40,40,40,55,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'RPAREN':([7,8,9,10,11,13,15,17,35,36,37,38,39,42,43,55,56,60,61,62,63,64,65,66,67,68,69,70,71,72,73,76,77,79,82,85,],[-18,-18,14,-9,-8,-11,-18,-10,-29,-32,-35,-36,-37,58,59,-18,73,-23,-24,-25,-26,-27,-28,-30,-31,-33,-34,76,-18,-5,-39,-38,-4,-7,-18,-6,]),'COMMA':([8,15,35,36,37,38,39,60,61,62,63,64,65,66,67,68,69,71,73,76,82,],[12,12,-29,-32,-35,-36,-37,-23,-24,-25,-26,-27,-28,-30,-31,-33,-34,78,-39,-38,78,]),'LBR':([14,58,59,],[16,74,75,]),'RBR':([16,19,20,21,22,23,24,25,31,44,57,74,75,80,81,83,84,],[-18,30,-18,-13,-14,-15,-16,-17,-12,-21,-22,-18,-18,83,84,-19,-20,]),'IF':([16,20,22,23,24,25,44,57,74,75,83,84,],[26,26,-14,-15,-16,-17,-21,-22,26,26,-19,-20,]),'WHILE':([16,20,22,23,24,25,44,57,74,75,83,84,],[27,27,-14,-15,-16,-17,-21,-22,27,27,-19,-20,]),'RETURN':([16,20,22,23,24,25,44,57,74,75,83,84,],[28,28,-14,-15,-16,-17,-21,-22,28,28,-19,-20,]),'ATTRIB':([18,],[29,]),'NUMBER':([28,29,32,33,40,45,46,47,48,49,50,51,52,53,54,55,78,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'SEMICOLON':([34,35,36,37,38,39,41,60,61,62,63,64,65,66,67,68,69,73,76,],[44,-29,-32,-35,-36,-37,57,-23,-24,-25,-26,-27,-28,-30,-31,-33,-34,-39,-38,]),'LT':([34,35,36,37,38,39,41,42,43,60,61,62,63,64,65,66,67,68,69,71,73,76,82,],[45,-29,-32,-35,-36,-37,45,45,45,45,45,45,45,45,45,-30,-31,-33,-34,45,-39,-38,45,]),'RT':([34,35,36,37,38,39,41,42,43,60,61,62,63,64,65,66,67,68,69,71,73,76,82,],[46,-29,-32,-35,-36,-37,46,46,46,46,46,46,46,46,46,-30,-31,-33,-34,46,-39,-38,46,]),'LTE':([34,35,36,37,38,39,41,42,43,60,61,62,63,64,65,66,67,68,69,71,73,76,82,],[47,-29,-32,-35,-36,-37,47,47,47,47,47,47,47,47,47,-30,-31,-33,-34,47,-39,-38,47,]),'RTE':([34,35,36,37,38,39,41,42,43,60,61,62,63,64,65,66,67,68,69,71,73,76,82,],[48,-29,-32,-35,-36,-37,48,48,48,48,48,48,48,48,48,-30,-31,-33,-34,48,-39,-38,48,]),'DOUBLEEQUALS':([34,35,36,37,38,39,41,42,43,60,61,62,63,64,65,66,67,68,69,71,73,76,82,],[49,-29,-32,-35,-36,-37,49,49,49,49,49,49,49,49,49,-30,-31,-33,-34,49,-39,-38,49,]),'NE':([34,35,36,37,38,39,41,42,43,60,61,62,63,64,65,66,67,68,69,71,73,76,82,],[50,-29,-32,-35,-36,-37,50,50,50,50,50,50,50,50,50,-30,-31,-33,-34,50,-39,-38,50,]),'PLUS':([35,36,37,38,39,56,66,67,68,69,73,76,],[51,-32,-35,-36,-37,51,-30,-31,-33,-34,-39,-38,]),'MINUS':([35,36,37,38,39,56,66,67,68,69,73,76,],[52,-32,-35,-36,-37,52,-30,-31,-33,-34,-39,-38,]),'TIMES':([36,37,38,39,68,69,73,76,],[53,-35,-36,-37,-33,-34,-39,-38,]),'DIVIDE':([36,37,38,39,68,69,73,76,],[54,-35,-36,-37,-33,-34,-39,-38,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'functions':([0,2,],[1,5,]),'function':([0,2,],[2,2,]),'empty':([0,2,7,8,15,16,20,55,71,74,75,82,],[3,3,10,13,13,21,21,72,79,21,21,79,]),'params':([7,],[9,]),'plist':([8,15,],[11,17,]),'statements':([16,20,74,75,],[19,31,80,81,]),'statement':([16,20,74,75,],[20,20,20,20,]),'attrib':([16,20,74,75,],[22,22,22,22,]),'if':([16,20,74,75,],[23,23,23,23,]),'while':([16,20,74,75,],[24,24,24,24,]),'return':([16,20,74,75,],[25,25,25,25,]),'logic':([28,29,32,33,45,46,47,48,49,50,55,78,],[34,41,42,43,60,61,62,63,64,65,71,82,]),'expression':([28,29,32,33,40,45,46,47,48,49,50,51,52,55,78,],[35,35,35,35,56,35,35,35,35,35,35,66,67,35,35,]),'term':([28,29,32,33,40,45,46,47,48,49,50,51,52,53,54,55,78,],[36,36,36,36,36,36,36,36,36,36,36,36,36,68,69,36,36,]),'call':([28,29,32,33,40,45,46,47,48,49,50,51,52,53,54,55,78,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'pcall':([55,],[70,]),'pclist':([71,82,],[77,85,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> functions","S'",1,None,None,None),
  ('functions -> function functions','functions',2,'p_func','parse.py',30),
  ('functions -> empty','functions',1,'p_func','parse.py',31),
  ('function -> FUNC ID LPAREN params RPAREN LBR statements RBR','function',8,'p_function','parse.py',42),
  ('pcall -> logic pclist','pcall',2,'p_params_call','parse.py',48),
  ('pcall -> empty','pcall',1,'p_params_call','parse.py',49),
  ('pclist -> COMMA logic pclist','pclist',3,'p_pclist','parse.py',58),
  ('pclist -> empty','pclist',1,'p_pclist','parse.py',59),
  ('params -> ID plist','params',2,'p_params','parse.py',67),
  ('params -> empty','params',1,'p_params','parse.py',68),
  ('plist -> COMMA ID plist','plist',3,'p_plist','parse.py',80),
  ('plist -> empty','plist',1,'p_plist','parse.py',81),
  ('statements -> statement statements','statements',2,'p_s','parse.py',89),
  ('statements -> empty','statements',1,'p_s','parse.py',90),
  ('statement -> attrib','statement',1,'p_statement','parse.py',97),
  ('statement -> if','statement',1,'p_statement','parse.py',98),
  ('statement -> while','statement',1,'p_statement','parse.py',99),
  ('statement -> return','statement',1,'p_statement','parse.py',100),
  ('empty -> <empty>','empty',0,'p_empty','parse.py',105),
  ('if -> IF LPAREN logic RPAREN LBR statements RBR','if',7,'p_if','parse.py',109),
  ('while -> WHILE LPAREN logic RPAREN LBR statements RBR','while',7,'p_while','parse.py',118),
  ('return -> RETURN logic SEMICOLON','return',3,'p_return','parse.py',130),
  ('attrib -> ID ATTRIB logic SEMICOLON','attrib',4,'p_attrib','parse.py',134),
  ('logic -> logic LT logic','logic',3,'p_logic_lt','parse.py',144),
  ('logic -> logic RT logic','logic',3,'p_logic_rt','parse.py',148),
  ('logic -> logic LTE logic','logic',3,'p_logic_lte','parse.py',152),
  ('logic -> logic RTE logic','logic',3,'p_logic_rte','parse.py',156),
  ('logic -> logic DOUBLEEQUALS logic','logic',3,'p_logic_de','parse.py',160),
  ('logic -> logic NE logic','logic',3,'p_logic_ne','parse.py',164),
  ('logic -> expression','logic',1,'p_logic_expression','parse.py',168),
  ('expression -> expression PLUS expression','expression',3,'p_e','parse.py',172),
  ('expression -> expression MINUS expression','expression',3,'p_expression_minus','parse.py',176),
  ('expression -> term','expression',1,'p_expression_term','parse.py',181),
  ('term -> term TIMES term','term',3,'p_term','parse.py',185),
  ('term -> term DIVIDE term','term',3,'p_term_div','parse.py',191),
  ('term -> call','term',1,'p_term_call','parse.py',196),
  ('term -> NUMBER','term',1,'p_term_number','parse.py',200),
  ('term -> ID','term',1,'p_term_id','parse.py',204),
  ('call -> ID LPAREN pcall RPAREN','call',4,'p_call','parse.py',214),
  ('term -> LPAREN expression RPAREN','term',3,'p_paren','parse.py',218),
]