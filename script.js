const rounds = [
  { target: 'mamá', options: ['mamá', 'memo', 'mima', 'mimo'] },
  { target: 'memo', options: ['mema', 'mama', 'memo', 'mimi'] },
  { target: 'mima', options: ['mimo', 'mima', 'mamá', 'meme'] },
  { target: 'pato', options: ['pato', 'peta', 'pata', 'pito'] },
  { target: 'luna', options: ['lina', 'luna', 'lana', 'lona'] }
];

const targetWordEl = document.getElementById('targetWord');
const optionsEl = document.getElementById('options');
const messageEl = document.getElementById('message');
const nextButton = document.getElementById('nextButton');

let currentRound = 0;

function shuffle(array) {
  return [...array].sort(() => Math.random() - 0.5);
}

function renderRound() {
  const round = rounds[currentRound];
  targetWordEl.textContent = round.target;
  messageEl.textContent = '';
  messageEl.className = 'message';
  optionsEl.innerHTML = '';

  shuffle(round.options).forEach((word) => {
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'word-option';
    btn.textContent = word;
    btn.addEventListener('click', () => handleChoice(word, round.target));
    optionsEl.appendChild(btn);
  });
}

function handleChoice(selected, target) {
  if (selected === target) {
    messageEl.textContent = `🎉 ¡Muy bien! Esa era la palabra "${target}". ¡Excelente trabajo!`;
    messageEl.className = 'message success';
  } else {
    messageEl.textContent = `❌ No, esa palabra significa "${selected}". Intenta nuevamente y busca la palabra "${target}".`;
    messageEl.className = 'message error';
  }
}

nextButton.addEventListener('click', () => {
  currentRound = (currentRound + 1) % rounds.length;
  renderRound();
});

renderRound();
