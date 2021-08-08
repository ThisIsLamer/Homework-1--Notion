import requests
import bs4

# Количество вопросов
# Ответы искать тут: https://www.edsys.in/general-knowledge-for-kids-105-questions-and-answers/#1
countQuestions = 4

class Question:
  def __init__(self, option):
    self.answer = option['answer']
    self.currentAnswer = option['currentAnswer']
    self.score = option['score']

    if self.answer == self.currentAnswer:
      self.answered = True,
      print(f'Ответ верный, получено: {self.score} баллов')
    else:
      print(f'Ответ неверный. Верный ответ - {self.currentAnswer}')

class main:
  def __init__(self):
    self.collection = {}
    self.questions = {}

  def parse(self):
    response = requests.get('https://www.edsys.in/general-knowledge-for-kids-105-questions-and-answers/#1').text
    
    soup = bs4.BeautifulSoup(response, 'html.parser').body

    questions = []
    questionData = soup.find_all('p')
    num = 0
    for i in questionData:
      i = str(i).replace('<p>', '').replace('</p>', '').split(' ')
      try:
        int(i[0].replace('.', ''))

        if num < 7:
          num += 1 
          continue

        del i[0]
        questions.append(' '.join(i))
      except:
        pass

    answers = []    
    answersData = soup.find_all('strong')
    for i in answersData:
      i = str(i).replace('<strong>', '').replace('</strong>', '')
      answer = i.split()
      if answer[0] in ['Answers:', 'Answer:', 'Ans:', 'Ans-']: answers.append(i.replace('Answer: ', '').replace('Answers: ', '').replace('Ans: ', '').replace('Ans- ', ''))

    for i in range(countQuestions):
      self.questions[i] = {
        'text': questions[i],
        'author': 'edsys',
        'level': 'Средне',
        'currentAnswer': answers[i],
        'topic': 'quest',
        'score': 10
      }


  def start(self):
    for i in self.questions:
      self.collection[i] = Question({
        'answer': str(input(f'Вопрос: {i}, тема: {self.questions[i]["topic"]}, сложность: {self.questions[i]["level"]}\n{self.questions[i]["text"]}\n> ')),
        'currentAnswer': self.questions[i]['currentAnswer'],
        'score': self.questions[i]['score']
      })
  def end(self):
    print('Вот и всё!')

    result = 0
    for i in self.collection:
      if self.collection[i].answered: result += 1

    print(f'Отвечено: {result} вопроса из {len(self.collection)}')

if __name__ == '__main__':
  fn = main()

  fn.parse()  
  fn.start()
  fn.end()
  