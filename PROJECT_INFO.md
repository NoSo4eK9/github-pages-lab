# 🚀 CyberLab - Interactive GitHub Pages Project

> Сучасний статичний сайт з інтерактивними можливостями на HTML, CSS, JavaScript та Python

![Version](https://img.shields.io/badge/version-2.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)

## ✨ Можливості

### 🎨 Frontend
- **Темна/Світла тема** - Зі збереженням вибору у `localStorage`
- **Плавні анімації** - CSS анімації та переходи
- **Адаптивний дизайн** - Оптимізовано для всіх пристроїв
- **Гарячі клавіші** - Навігація стрілками (←, →)
- **Інтерактивні карточки** - Ефекти при наведенні

### ⚙️ JavaScript
```javascript
// Основні класи та функціональність:
- ThemeManager        // Управління темою
- Counter            // Анімовані лічильники
- SmoothScroll       // Плавна прокрутка
- PageTransition     // Переходи між сторінками
- AnimationObserver  // Спостереження за анімаціями
- KeyboardNav        // Клавіатурна навігація
- FormValidator      // Валідація форм
- PerfMonitor        // Моніторинг продуктивності
```

### 🐍 Python

#### Запуск аналізу проєкту:
```bash
python utils.py analyze
```

**Результат:**
```
📊 Аналіз проєкту CyberLab

📁 Файли проєкту
├─ HTML Файли: 3
├─ CSS Файли: 1
├─ JS Файли: 1
├─ Всього Файлів: 5
└─ Загальний розмір: 45.32 KB

📄 HTML Структура
├─ Сторінок: 3
├─ Всього Елементів: 156
├─ Текстовий контент: 2845 символів
└─ Сторінки:
    • index.html: 52 елемента
    • about.html: 48 елементів
    • projects.html: 56 елементів

🎨 CSS Стилізація
├─ Таблиці стилів: 1
├─ CSS Правила: 45
├─ CSS Змінні: 12
├─ Анімації: 5
└─ Рядків Коду: 312

⚙️  JavaScript
├─ Скрипти: 1
├─ Класи: 8
├─ Функції: 25
└─ Рядків Коду: 487

🔗 Аналіз Посилань
├─ Внутрішні посилання: 8
├─ Зовнішні посилання: 2
└─ Невалідні посилання: 0
```

#### Експортувати звіт у JSON:
```bash
python utils.py analyze --export
```

#### Генерувати метадані для SEO:
```bash
python utils.py metadata
```

#### Генерувати sitemap:
```bash
python utils.py sitemap
```

## 📁 Структура проєкту

```
github-pages-lab/
├── index.html           # Головна сторінка
├── about.html           # Інформаційна сторінка
├── projects.html        # Сторінка проєктів
├── styles.css           # Основні стилі (оновлено)
├── script.js            # JavaScript код (новий)
├── utils.py             # Python утиліта (новий)
├── README.md            # Цей файл
└── sitemap.xml          # Карта сайту (генерується)
```

## 🎯 Нові можливості в версії 2.0

### ✅ Темна/Світла тема
Натисніть кнопку 🌙/☀️ у верхньому правому куті для перемикання теми.

**Код:**
```javascript
new ThemeManager(); // Автоматично активується при завантаженні
```

### ✅ Клавіатурна навігація
- `←` - Попередня сторінка
- `→` - Наступна сторінка

### ✅ Плавні переходи
Всі переходи між сторінками має плавний ефект затемнення.

### ✅ Анімовані карточки
Карточки спливають при прокрутці з затримкою.

```css
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

## 🚀 Розгортання на GitHub Pages

### Крок 1: Завантажити код до GitHub
```bash
git init
git add .
git commit -m "CyberLab v2.0 - Interactive website"
git branch -M main
git remote add origin https://github.com/ВАШ_КОРИСТУВАЧ/github-pages-lab.git
git push -u origin main
```

### Крок 2: Активувати GitHub Pages
1. Перейти на Settings репозиторію
2. Обрати "Pages" в лівому меню
3. Вибрати "main" гілку та папку "root"
4. Натиснути "Save"

### Крок 3: Ваш сайт готовий! 🎉
Сайт буде доступний за адресою:
```
https://ВАШ_КОРИСТУВАЧ.github.io/github-pages-lab/
```

## 📱 響ивна адаптація

Сайт оптимізований для всіх розмірів екранів:
- 📱 Mobile (320px - 640px)
- 📱 Tablet (641px - 1024px)
- 🖥️ Desktop (1025px+)

## 🛠️ Вимоги

### Frontend
- Сучасний браузер з підтримкою:
  - CSS Grid / Flexbox
  - Intersection Observer API
  - CSS Custom Properties (CSS Variables)

### Backend (Python)
- Python 3.7+
- Вбудовані модулі (не потрібні додаткові залежності)

## 📊 Моніторинг продуктивності

JavaScript автоматично логує метрики продуктивності в консоль:

```
🚀 Метрики Продуктивності:
├─ DOM Ready: 245ms
├─ Page Load: 1230ms
└─ Статус: ✅ Excellent
```

## 🔧 Налаштування

### Змінити тему за замовчуванням
В `script.js`, змініть:
```javascript
this.theme = localStorage.getItem('theme') || 'dark';
// На:
this.theme = localStorage.getItem('theme') || 'light';
```

### Налаштувати барви
В `styles.css`, змініть CSS змінні:
```css
:root {
  --accent: #4ee1a0;      /* Основний колір */
  --accent-2: #5cc8ff;    /* Вторинний */
  --accent-3: #ff6b9d;    /* Третинний */
}
```

## 📝 Статистика коду

| Метрика | Значення |
|---------|---------|
| HTML Елементів | 156 |
| CSS Правил | 45+ |
| CSS Анімацій | 5 |
| JS Класів | 8 |
| JS Функцій | 25+ |
| Загальний розмір | ~45 KB |
| Анімацій | 10+ |

## 🤝 Контрибьютінг

Ви можете покращити проєкт:
1. Fork репозиторію
2. Створити гілку (`git checkout -b feature/improvement`)
3. Commit змін (`git commit -m 'Add improvement'`)
4. Push до гілки (`git push origin feature/improvement`)
5. Відкрити Pull Request

## 📚 Додаткові ресурси

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [MDN Web Docs](https://developer.mozilla.org/)
- [CSS-Tricks](https://css-tricks.com/)
- [JavaScript.info](https://javascript.info/)

## 📄 Ліцензія

MIT License - дивіться [LICENSE](LICENSE) для деталей.

## 👨‍💻 Автор

**CyberLab Team** - Навчальний проєкт для демонстрації веб-розробки

---

**Версія:** 2.0 | **Останнє оновлення:** 21.05.2026 | **Статус:** ✅ Active

> ⭐ Якщо вам сподобався проєкт, дайте йому зірку на GitHub!
