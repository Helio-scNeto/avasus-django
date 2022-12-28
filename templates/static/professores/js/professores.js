function exibir_form(tipo) {
  addProf = document.getElementById('addProf');
  attProf = document.getElementById('attProf');

  if (tipo == 1) {
    attProf.style.display = 'none';
    addProf.style.display = 'block';
  } else if (tipo == 2) {
    addProf.style.display = 'none';
    attProf.style.display = 'block';
  }
}

function dadosProf() {
  let professor = document.getElementById('selectProf');
  let csrf_token = document.querySelector(
    '[name=csrfmiddlewaretoken]'
  ).value;
  idProf = professor.value;
  data = new FormData();
  data.append('idProf', idProf);

  fetch('/professores/attProf/', {
    method: 'POST',
    headers: {
      'X-CSRFToken': csrf_token,
    },
    body: data,
  })
    .then(function (result) {
      return result.json();
    })
    .then(function (data) {
      document.getElementById('formAttProf').style.display = 'block';

      const nome = document.getElementById('nome');
      nome.value = data['professor']['nome'];

      const nomeSocial = document.getElementById('nomeSocial');
      nomeSocial.value = data['professor']['nomeSocial'];

      const estado = document.getElementById('estado');
      estado.value = data['professor']['estado'];

      const cidade = document.getElementById('cidade');
      cidade.value = data['professor']['cidade'];

      const cpf = document.getElementById('cpf');
      cpf.value = data['professor']['cpf'];

      const senha = document.getElementById('senha');
      senha.value = data['professor']['senha'];

      aniversario = document.getElementById('aniversario');
      aniversario.value = data['professor']['aniversario'];
    });
}
