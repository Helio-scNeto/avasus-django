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

      nome = document.getElementById('nome');
      nome.value  = data['nome'];

      nomeSocial = document.getElementById('nomeSocial');
      nomeSocial.value = data['nomeSocial'];

      estado = document.getElementById('estado');
      estado.value = data['estado'];

      cidade = document.getElementById('cidade');
      cidade.value = data['cidade'];

      cpf = document.getElementById('cpf');
      cpf.value = data['cpf'];

      senha = document.getElementById('senha');
      senha.value = data['senha'];

      aniversario = document.getElementById('aniversario');
      aniversario.value = data['aniversario'];
    });
}
