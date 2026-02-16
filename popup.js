const nomeInput = document.getElementById('nome');
const testarButton = document.getElementById('testar');
const resultado = document.getElementById('resultado');

function exibirMensagem() {
  const nome = nomeInput.value.trim();

  if (!nome) {
    resultado.textContent = 'Digite seu nome para continuar.';
    return;
  }

  resultado.textContent = `Olá, ${nome}! Teste realizado com sucesso ✅`;
}

testarButton.addEventListener('click', exibirMensagem);
nomeInput.addEventListener('keydown', (event) => {
  if (event.key === 'Enter') {
    exibirMensagem();
  }
});