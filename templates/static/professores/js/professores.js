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

      const id = document.getElementById('id');
      id.value = data['profIdJson'];

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

function updateProf() {
  id = document.getElementById('id').value;
  nome = document.getElementById('nome').value;
  nomeSocial = document.getElementById('nomeSocial').value;
  cidade = document.getElementById('cidade').value;
  estado = document.getElementById('estado').value;
  cpf = document.getElementById('cpf').value;
  aniversario = document.getElementById('aniversario').value;
  senha = document.getElementById('senha').value;

  fetch('/professores/updateProf/' + id, {
    method: 'POST',
    headers: {
      
    },
    body: JSON.stringify({
      nome: nome,
      nomeSocial: nomeSocial,
      cidade: cidade,
      estado: estado,
      cpf: cpf,
      aniversario: aniversario,
      senha: senha,
    }),
  })
    .then(function (result) {
      return result.json();
    })
    .then(function (data) {
      if(data['status'] == '200') {
        const nome = data['nome']
        const nomeSocial = data['nomeSocial']
        const cidade = data['cidade']
        const estado = data['estado']
        const cpf = data['cpf']
        const aniversario = data['aniversario']
        const senha = data['senha']
        window.alert('Dados alterado com sucesso!')
      }
      else {
        window.alert('Ocorreu algum erro')
      }
    });
}
