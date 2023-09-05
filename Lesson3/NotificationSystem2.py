#Шаблон Наблюдатель:
#Реализуйте паттерн Наблюдатель на языке Python для системы уведомлений. 
#Создайте класс NotificationSystem (наблюдаемый объект), 
#который будет иметь методы для добавления наблюдателей и уведомления о событиях. 
#Создайте несколько наблюдателей, реагирующих на уведомления.

#Вариант решения 2. 
#Практическое применение шаблона Наблюдатель в виде рассылки события всем слушателям нажатием по кнопке:

class Observer {
	subscribers = [];

	constructor() {
		if (!Observer.instance) {
			Observer.instance = this;
		}
		return Observer.instance;
	}

	subscribe(subscriber) {
		this.subscribers.push(subscriber);
		return this;
	}

	unsubscribe(subscriber) {
		this.subscribers.filter(sub => sub !== subscriber);
		return this;
	}

	notify(payload) {
		this.subscribers.forEach(subscriber => subscriber(payload));
		return this;
	}
}

// определим первого слушателя
function logToConsole(message) {
	console.log(message);
}
// и второго
function logToDom(message) {
	const logsContainer = document.getElementById('observer-logs');
	logsContainer.innerHTML += `<li>${message}</li>`;
}

const btn = document.getElementById('btn');

const observer = new Observer();

// подписываем двух слушателей на observer
const subscribers = [logToConsole, logToDom];

subscribers.forEach(subscriber => observer.subscribe(subscriber));

// выполняем оповещение при нажатии на кнопку 
btn.addEventListener('click', e => {
	e.preventDefault();
	observer.notify('btn clicked');
})