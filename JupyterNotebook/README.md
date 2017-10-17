# Реализованные метрические алгоритмы классификации
***
**ONN** - алгоритм классификации по ближайшему соседу

Принцип работы: в выборке происходит поиск ближайшего к классифицируемому объекта, класс найденного объекта и является результатом классификации.

Реализация алгоритма представлена в файле [*IrisONN.ipynb*](https://github.com/TillZas/University/blob/master/JupyterNotebook/IrisONN.ipynb)

Пример работы:

![Пример работы классификатора](https://github.com/TillZas/University/blob/master/JupyterNotebook/IrisONN.png)

***

**KNN** - алгоритм классификации по **k** ближайшим соседам

Принцип работы: в выборке происходит поиск к ближайших к классифицируемому объектов, класс, наибольшее количество объектов которого, было найдено и является результатом классификации.

Реализация алгоритма представлена в файле [*IrisKNN.ipynb*](https://github.com/TillZas/University/blob/master/JupyterNotebook/IrisKNN.ipynb)

Пример работы (при оптимальном **k** = 31):

![Пример работы классификатора](https://github.com/TillZas/University/blob/master/JupyterNotebook/IrisKNN.png)

***

**ParsenWindow** - алгоритм классификации методом парзеновского окна

Принцип работы: Вводится невозрастающая функция ядра *K(z)* и число **h != 0** обозначающее ширину "окна".
Каждому элементу выборки x_i ставится в соответствии число *P_i = K(p(x_i,u)/h)*, где u это классифицируемый элемент а p(a,b) функция расстояния между a и b. Результатом работы классификатора является класс, сумма значений *P_i* элементов которого наибольшая.

Реализация алгоритма представлена в файле [*ParsenWindow.ipynb*](https://github.com/TillZas/University/blob/master/JupyterNotebook/ParsenWindow.ipynb)

Пример работы:

![Пример работы классификатора](https://github.com/TillZas/University/blob/master/JupyterNotebook/ParsenWindow.png)

***

**Potential Function** - алгоритм классификации методом потенциальных функций

Принцип работы: Вводится невозрастающая функция ядра *K(z)* и массивы **h** и **t** обозначающее ширину "окна" и потенциал для кждого элемента соответственно.
Каждому элементу выборки x_i ставится в соответствии число *P_i = t_i*K(p(x_i,u)/h_i)*, где u это классифицируемый элемент а p(a,b) функция расстояния между a и b. Результатом работы классификатора является класс, сумма значений *P_i* элементов которого наибольшая.

Реализация алгоритма представлена в файле [*PotentialFunction.ipynb*](https://github.com/TillZas/University/blob/master/JupyterNotebook/PotentialFunction.ipynb)

Пример работы:

![Пример работы классификатора](https://github.com/TillZas/University/blob/master/JupyterNotebook/PotentialFunction.png)


***
Литература:

*[К.В. Воронцов  Математические методы обучения по прецедентам (теория обучения машин)](https://github.com/TillZas/University/blob/master/JupyterNotebook/Voron-ML-1.pdf)
