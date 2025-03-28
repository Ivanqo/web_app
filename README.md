<h1 align="center">🎓 Student Helper MGSU</h1>

<h3 align="center">Веб-приложение для организации учебного процесса студентов</h3>

<div align="center">
  <img src="https://img.shields.io/badge/Django-3.2-green?logo=django" alt="Django">
  <img src="https://img.shields.io/badge/Python-3.9-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Status-Alpha-orange" alt="Статус">
</div>

<div align="center">
  <img src="https://github.com/yourusername/student-helper/raw/main/docs/demo-screenshot.png" width="700" alt="Главный интерфейс">
</div>

<h2>📌 Идея проекта</h2>

<p>Разработанное в рамках курса "Веб-программирование" в <strong>Московском Государственном Строительном Университете</strong>, это приложение призвано помочь студентам в организации учебного процесса. Основная цель - объединить все необходимые инструменты в одном месте.</p>

<h2>✨ Ключевые возможности</h2>

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px;">
  <div>
    <h4>📅 Учебное расписание</h4>
    <ul>
      <li>Интеллектуальное напоминание о занятиях</li>
      <li>Календарь дедлайнов</li>
    </ul>
  </div>
  <div>
    <h4>✏️ Новостная лента</h4>
    <ul>
      <li>Актуальные новости</li>
      <li>Интересные короткие видео</li>
    </ul>
  </div>
</div>

<h2>🛠 Технологии</h2>

<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 20px;">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" height="28">
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" height="28">
  <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white" height="28">
  <img src="https://img.shields.io/badge/Chart.js-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white" height="28">
</div>

<h2>🚀 Быстрый старт</h2>

<h3>Предварительные требования</h3>
<ul>
  <li>Python 3.9+</li>
  <li>SQLITE</li>
</ul>

<h3>Установка</h3>
<pre><code># Клонирование репозитория
git clone https://github.com/yourusername/student-helper.git
cd student-helper

# Создание виртуального окружения
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

# Установка зависимостей
pip install -r requirements.txt

# Настройка окружения
cp .env.example .env
# Заполните .env своими настройками

# Запуск миграций
python manage.py migrate

# Создание суперпользователя
python manage.py createsuperuser

# Запуск сервера
python manage.py runserver
</code></pre>

<h2>📸 Скриншоты</h2>

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px; margin: 20px 0;">
  <div>
    <img src="![image](https://github.com/user-attachments/assets/297efffd-7d72-4200-887e-fd3b1da89fa7)" alt="Расписание">
    <p><em>Интерфейс расписания</em></p>
  </div>
  <div>
    <img src="https://github.com/yourusername/student-helper/raw/main/docs/materials-screenshot.png" alt="Материалы">
    <p><em>Система учебных материалов</em></p>
  </div>
</div>

<h2>📊 Roadmap</h2>

<ul>
  <li><input type="checkbox" checked> Базовая система расписания</li>
  <li><input type="checkbox" checked> Хранение учебных материалов</li>
  <li><input type="checkbox"> WEB приложение</li>
</ul>

<h2>👨‍💻 Разработчики</h2>

<p>Проект разработан студентами <strong>МГСУ</strong> кафедры "Информационные системы и технологии":</p>
<ul>
  <li>Басенко Иван (Fullstack) - <b>Teamlead</b></li>
  <li>Дищенко Дмитрий (Fullstack)</li>
  <li>Гончаров Пётр (designer)</li>
  <li>Капытин Андрей (backend)</li>
</ul>

<h2>📝 Лицензия</h2>

<p>MIT License © 2023 Student Helper Team</p>

<div align="center" style="margin-top: 40px;">
  <p>Проект разработан в рамках учебного курса МГСУ</p>
  <img src="https://github.com/yourusername/student-helper/raw/main/docs/mgsu-logo.png" width="150" alt="Лого МГСУ">
</div>
