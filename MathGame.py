import os, pickle, random, getpass

class MathGame:
	def __init__(self, name):

		user = getpass.getuser()
		
		try:
			os.chdir(f'/storage/emulated/0')
		
		except:
			os.chdir(f'C:\\{user}')
			
		if not os.path.exists('MathGame'):
			os.mkdir('MathGame')
			
		os.chdir('MathGame')
		
		if not os.path.exists('MGD.dat'):
			self.data = {'name' : name, 'lvl' : 1,
								 'skin' : '(>_<)',
								 'pull' : 100,
								 'ques' : 1}
								 
								 
		else:
			file = open('MGD.dat', 'rb')
			self.data = pickle.load(file)
			file.close()
			
		self._range_for_stars_ = 10
		self._range_for_plus_ = 10
		
		skins = ['(>_<)', '(+_+)', '(*_*)',
					  '(×_×)', '{°_°}', '{-_-}',
					  '(o_o)', '($_$)', '{p_q}',
					  '{b_d}', '{v_v}', '[=_=]',
					  '{O_O}', '(0_0)', '(8_8)',
					  '(s_s)', '(H_H)', '{m_m}',
					  '[÷_÷]', '{w_w}', '[u_u]']
					  
		self.make_question()
		
		self.data['skin'] = skins[self.data['lvl']]
		
		
	def make_question(self):		
		self.questions = [self.question_star,
		self.question_slash,
		self.question_plus,
		self.question_taf,
		self.question_tav,
		self.question_jasr,
		self.star_slash,
		self.star_plus,
		self.star_taf,
		self.star_tav,
		self.star_jasr,
		self.slash_plus,
		self.slash_taf,
		self.slash_tav,
		self.slash_jasr,
		self.plus_taf,
		self.plus_tav,
		self.plus_jasr,
		self.taf_tav,
		self.taf_jasr,
		self.tav_jasr,
		self.star_slash_plus,
		self.star_slash_taf,
		self.star_slash_tav,
		self.star_slash_jasr,
		self.slash_plus_taf,
		self.slash_plus_tav,
		self.slash_plus_jasr,
		self.plus_taf_tav,
		self.plus_taf_jasr,
		self.taf_tav_jasr,
		self.star_slash_plus_taf,
		self.star_slash_plus_tav,
		self.star_slash_plus_jasr,
		self.slash_plus_taf_tav,
		self.slash_plus_taf_jasr,
		self.plus_taf_tav_jasr,
		self.star_slash_plus_taf_tav,
		self.star_slash_plus_taf_jasr,
		self.star_slash_plus_taf_tav_jasr]
		
		range_ = self.data['ques'] // 3
			
		self.data['lvl'] = range_
			
		self.question = self.questions[0 : range_ + 1]
			
		self.data['pull'] += range_ * 50
			
		ques = random.choice(self.question)
			
		ques()
	
			
	def question_star(self):
		num1 = random.randint(2, self._range_for_stars_)
		num2 = random.randint(2, self._range_for_stars_)
		self.ques = f'{num1} × {num2}'
		
		
	def question_slash(self):
		num1 = random.randint(2, self._range_for_stars_)
		
		num2 = random.randint(2, self._range_for_stars_)
		
		self.ques = f'{num1 * num2} ÷ {num2}'
		
			
	def question_plus(self):
		num1 = random.randint(2, 200)
		
		num2 = random.randint(2, 50)
		
		num3 = random.randint(1, 100)
		self.ques = f'{num1} + {num2} + {num3}'
		
		
	def question_taf(self):
		num1 = random.randint(2, 200)
		
		num2 = random.randint(2, 50)
		
		self.ques = f'{num1} - {num2}'
		
	
	def question_tav(self):
		num1 = random.randint(2, 10)
		
		self.ques = f'{num1} ^ 2'
		
	
	def question_jasr(self):
		num1 = random.randint(2, 10)
		
		self.ques = f'({num1**2})jasr'
		
	
	def star_slash(self):
		num1 = random.randint(2, self._range_for_stars_)
		
		num2 = random.randint(2, self._range_for_stars_)
		
		num3 = random.randint(2, self._range_for_stars_)
		
		self.ques = f'{num1* num2} ÷ {num2} × {num3}'
		
		
	def star_plus(self):
		num1 = random.randint(2, self._range_for_stars_)
		
		num2 = random.randint(2, self._range_for_stars_)
		
		num3 = random.randint(2, self._range_for_plus_)
		
		self.ques = f'{num1} × {num2} + {num3}'	
		
						
	def star_taf(self):
		num1 = random.randint(2, self._range_for_stars_)
		
		num2 = random.randint(2, self._range_for_stars_)
		
		num3 = random.randint(2, self._range_for_plus_)
		
		self.ques = f'{num1} × {num2} - {num3}'		
		
				
	def star_tav(self):
		num1 = random.randint(2, self._range_for_stars_)
		
		num2 = random.randint(2, self._range_for_stars_)
		

		
		self.ques = f'{num1} × {num2} ^ 2'	
		
				
	def star_jasr(self):
		num1 = random.randint(2, self._range_for_stars_)
		
		num2 = random.randint(2, self._range_for_stars_)
		
		num3 = random.randint(2, 10)
		
		self.ques = f'{num1} × {num2} + ({num3**2})jasr'	
		
		
	def slash_plus(self):
		num1 = random.randint(2, self._range_for_stars_)
		
		num2 = random.randint(2, self._range_for_stars_)
		
		num3 = random.randint(2, self._range_for_plus_)
		
		self.ques = f'{num1*num2} ÷ {num2} + {num3}'	
		
		
	def slash_taf(self):
		num1 = random.randint(2, self._range_for_stars_)
		
		num2 = random.randint(2, self._range_for_stars_)
		
		num3 = random.randint(2, self._range_for_plus_)
		
		self.ques = f'{num1*num2} ÷ {num2} - {num3}'	
		
		
	def slash_tav(self):
		num1 = random.randint(2, self._range_for_stars_)
		
		num2 = random.randint(2, 10)
		
		self.ques = f'{num1*num2} ÷ {num2} ^ 2'	
		
	
	def slash_jasr(self):
		num1 = random.randint(2, self._range_for_stars_)
		
		num2 = num1 = random.randint(1, 10)
		
		self.ques = f'{num1*num2} ÷ ({num2**2})jasr'	
		
			
	def plus_taf(self):
		num1 = random.randint(2, self._range_for_plus_)
		
		num2 =random.randint(2, self._range_for_plus_)
		
		num3 = random.randint(2, self._range_for_plus_)
		
		self.ques = f'{num1} + {num2} - {num3}'		
		
		
	def plus_tav(self):
		num1 = random.randint(2, self._range_for_plus_)
		
		num2 = random.randint(2, self._range_for_plus_)
		
		self.ques = f'{num1} + {num2} ^ 2'	
		
		
	def plus_jasr(self):
		num1 = random.randint(2, self._range_for_plus_)
		
		num2 = random.randint(2, self._range_for_plus_)
		
		self.ques = f'{num1} + ({num2**2})jasr'	
		
		
	def taf_tav(self):
		num1 = random.randint(2, self._range_for_plus_)
		
		num2 = random.randint(2, self._range_for_plus_)
		
		self.ques = f'{num1} - {num2} ^ 2'	
		
		
	def taf_jasr(self):
		num1 = random.randint(2, self._range_for_plus_)
		
		num2 = random.randint(2, self._range_for_plus_)
		
		self.ques = f'{num1} - ({num2**2})jasr'	
				
	
	def tav_jasr(self):
		num1 = random.randint(2, self._range_for_plus_)
		
		num2 = random.randint(2, self._range_for_plus_)
		
		self.ques = f'{num1} - ({num2**2})jasr'	
		
		
	def star_slash_plus(self):
		num1 = random.randint(2, self._range_for_plus_)
		
		num2 = random.randint(2, self._range_for_stars_)
		
		num3 = random.randint(2, self._range_for_stars_)
		
		num4 = random.randint(2, self._range_for_stars_)
		
		self.ques = f'{num4} × {num2*num3} ÷ {num3} + {num1}'
		
		
	def star_slash_taf(self):
		num1 = random.randint(2, self._range_for_plus_)
		
		num2 = random.randint(2, self._range_for_stars_)
		
		num3 = random.randint(2, self._range_for_stars_)
		
		num4 = random.randint(2, self._range_for_stars_)
		
		self.ques = f'{num4} × {num2*num3} ÷ {num3} - {num1}'
		
		
	def star_slash_tav(self):		
		num2 = random.randint(2, self._range_for_stars_)
		
		num3 = random.randint(2, self._range_for_stars_)
		
		num4 = random.randint(2, self._range_for_stars_)
		
		self.ques = f'{num4} × {num2*num3} ÷ {num3} ^ 2'
		
		
	def star_slash_jasr(self):
		num2 = random.randint(2, self._range_for_stars_)
		
		num3 = random.randint(2, self._range_for_stars_)
		
		num4 = random.randint(2, self._range_for_stars_)
		
		self.ques = f'{num4} × {num2*num3} ÷ {num3} ^ 2'
		
		
	def slash_plus_taf(self):
		num1 = random.randint(2, self._range_for_plus_)
		
		num2 = random.randint(2, self._range_for_stars_)
		
		num3 = random.randint(2, self._range_for_stars_)
		
		num4 = random.randint(2, self._range_for_stars_)
		
		self.ques = f'{num4*num2} ÷ {num2} + {num3} - {num1}'
		
		
	def slash_plus_tav(self):		
		num2 = random.randint(2, self._range_for_stars_)
		
		num3 = random.randint(2, self._range_for_stars_)
		
		num4 = random.randint(2, self._range_for_stars_)
		
		self.ques = f'{num4*num2} ÷ {num2} + {num3} ^ 2'
		
		
	def slash_plus_jasr(self):
		num1 = random.randint(2, self._range_for_plus_)
		
		num2 = random.randint(2, self._range_for_stars_)
		
		num3 = random.randint(2, self._range_for_stars_)
		
		num4 = random.randint(2, self._range_for_stars_)
		
		self.ques = f'{num4*num2} ÷ {num2} + ({num3**2})jasr'
		
	
	def plus_taf_tav(self):		
		num2 = random.randint(2, self._range_for_plus_)
		
		num3 = random.randint(2, self._range_for_plus_)
		
		num4 = random.randint(2, self._range_for_plus_)
		
		self.ques = f'{num4} + {num2} - {num3} ^ 2'
		
		
	def plus_taf_jasr(self):
		num2 = random.randint(2, self._range_for_plus_)
		
		num3 = random.randint(2, self._range_for_plus_)
		
		num4 = random.randint(2, self._range_for_plus_)
		
		self.ques = f'{num4} + {num2} - {num3})jasr'
		
		
	def taf_tav_jasr(self):		
		num2 = random.randint(2, self._range_for_stars_)
		
		num3 = random.randint(2, self._range_for_stars_)
		
		self.ques = f'{num2} ^ 2 - ({num3**2})jasr'
		
		
	def star_slash_plus_taf(self):
		num1 = random.randint(2, self._range_for_stars_)
		
		num2 = random.randint(2, self._range_for_stars_)
		
		num3 = random.randint(2, self._range_for_plus_)
		
		num4 = random.randint(2, self._range_for_plus_)
		
		num5 = random.randint(2, self._range_for_stars_)
		
		self.ques = f'{num3} - {num1} × ({num2*num5} ÷ {num5}) + {num4}'
		
		
	def star_slash_plus_tav(self):
		num1 = random.randint(2, self._range_for_stars_)
		
		num2 = random.randint(2, self._range_for_stars_)
		
		num4 = random.randint(2, self._range_for_plus_)
		
		num5 = random.randint(2, self._range_for_stars_)
		
		self.ques = f'{num1} × ({num2*num5} ÷ {num5}) + {num4} ^ 2'
				
		
	def star_slash_plus_jasr(self):
		num1 = random.randint(2, self._range_for_stars_)
		
		num2 = random.randint(2, self._range_for_stars_)
		
		num4 = random.randint(2, self._range_for_plus_)
		
		num5 = random.randint(2, self._range_for_stars_)
		
		self.ques = f'{num1} × ({num2*num5} ÷ {num5}) + ({num4**2})jasr'
		
		
	def slash_plus_taf_tav(self):		
		num2 = random.randint(2, self._range_for_stars_)
		
		num3 = random.randint(2, self._range_for_plus_)
		
		num4 = random.randint(2, self._range_for_plus_)
		
		num5 = random.randint(2, self._range_for_stars_)
		
		self.ques = f'{num3} - ({num2*num5} ÷ {num5}) + {num4} ^ 2'		
		
		
	def slash_plus_taf_jasr(self):
		num2 = random.randint(2, self._range_for_stars_)
		
		num3 = random.randint(2, self._range_for_plus_)
		
		num4 = random.randint(2, self._range_for_plus_)
		
		num5 = random.randint(2, self._range_for_stars_)
		
		self.ques = f'{num3} - ({num2*num5} ÷ {num5}) + ({num4})jasr'
		
		
	def plus_taf_tav_jasr(self):
		num2 = random.randint(2, self._range_for_stars_)
		
		num3 = random.randint(2, self._range_for_plus_)
		
		num4 = random.randint(2, self._range_for_plus_)
		
		self.ques = f'{num3} - {num2} ^ 2 + ({num4})jasr'
		
		
	def star_slash_plus_taf_tav(self):
		num1 = random.randint(2, self._range_for_stars_)
		
		num2 = random.randint(2, self._range_for_stars_)
		
		num3 = random.randint(2, self._range_for_plus_)
		
		num4 = random.randint(2, self._range_for_plus_)
		
		num5 = random.randint(2, self._range_for_stars_)
		
		self.ques = f'{num1} × ({num2*num5} ÷ {num5}) + {num4} ^ 2 - {num3}'
		
		
	def star_slash_plus_taf_jasr(self):
		num1 = random.randint(2, self._range_for_stars_)
		
		num2 = random.randint(2, self._range_for_stars_)
		
		num3 = random.randint(2, self._range_for_plus_)
		
		num4 = random.randint(2, self._range_for_plus_)
		
		num5 = random.randint(2, self._range_for_stars_)
		
		self.ques = f'{num1} × ({num2*num5} ÷ {num5}) + ({num4**2})jasr - {num3}'
		
		
	def star_slash_plus_taf_tav_jasr(self):
		num1 = random.randint(2, self._range_for_stars_)
		
		num2 = random.randint(2, self._range_for_stars_)
		
		num3 = random.randint(2, self._range_for_plus_)
		
		num4 = random.randint(2, self._range_for_plus_)
		
		num5 = random.randint(2, self._range_for_stars_)		
		
		self.ques = f'{num1} × ({num2*num5} ÷ {num5}) + ({num4**2})jasr - {num3} ^ 2'
		
		
	def check(self, result):
		answer = ''
		for char in self.ques:
			match char:
				case '×':
					answer += '*'
					
				case '÷':
					answer += '/'
					
				case '^':
					answer += '**'
					
				case 'jasr':
					answer += '** 0.5'
					
			if not char in ['×', '÷', '^', 'jasr']:
				answer += char
				
		self.answer = eval(answer)

		if result == self.answer:
			self.data['pull'] += 10
			self.data['ques'] += 1
			self._range_for_plus_ += 1
			self._range_for_stars_ += 1
			return True
			
		else:
			self.data['pull'] -= 15
			return False
			
	def save(self):
		file = open('MGD.dat', 'wb')
		pickle.dump(self.data, file)
		file.close()


while True:	
	app = MathGame('ali')	
		
	print(f'''your skin: {app.data['skin']}''')
	
	print(f'''your level: {app.data['lvl']}''')
	
	print(f'''your pull: {app.data['pull']}''')
	
	app.make_question()
	question = app.ques
	print(f'my question: {question}')
	answer = int(input('what is your answer? '))
	print(app.data['ques'])
	if answer != 'exit':
			result = app.check(answer)
			if result:
				print('your answer was true!')
				
			else:
				print('your answer was false!')			
			
			print('-'*30)	
			
	else:
			break
			
	app.save()
