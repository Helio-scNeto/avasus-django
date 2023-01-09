$(document).ready(function(){
  // Cadastro
  $('.mask-cpf').mask('000.000.000-00', {reverse: true});
  $('.mask-aniversario').mask('00/00/0000 00:00:00');

  // Login
  $('#id_username').mask('000.000.000-00', {reverse: true});
})

