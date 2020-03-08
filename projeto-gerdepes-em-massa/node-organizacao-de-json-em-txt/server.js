// PARA EXECUTAR A APLICAÇÃO INSTALE O NODEJS
// CONFIGURE E SALVE O ARQUIVO [] COM AS CONFIGURAÇÕES ABAIXO
// --------------
// C:\[path]\.npmrc
// --------------
// strict-ssl=false
// registry=http://registry.npmjs.org
// **************
// CERTIFIQUE-SE DE TER INSTALADO AS DEPENDENDIAS ABAIXO
// --------------
// Dependencias
// --------------
// npm install express
// npm install body-parser
// npm install fs
// **************
// EXECUTE O PROJETO EXECUTANDO O COMANDO [NPM START] NO PROMPT DE COMANDO

var express = require('express');
var bodyParser = require('body-parser');
var fs = require('fs');

var app = express();

app.use(bodyParser.urlencoded({ extended:true }));
app.use(bodyParser.json());

app.use(function(req, res, next){
 res.setHeader("Access-Control-Allow-Origin", "*");
 res.setHeader("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE");
 res.setHeader("Access-Control-Allow-Headers", "content-type");
 res.setHeader("Content-Type", "application/json");
 res.setHeader("Access-Control-Allow-Credentials", true);
 next();
});

app.listen(9090, function(){ console.log('Servidor Web rodando na porta 9090') });

// Buscar Usuario
app.get('/', function(req, res){
	fs.readFile('json/people.json', 'utf8', function(err, data){
		var oJson = JSON.parse(data);
		var lenJson = oJson.people.length;

		// exibição de dados do JSON em terminal Javascript / NodeJS
		// console.log("len " + lenJson);
	    
	    // Salvamento de dados do JSON em TXT
		for(var i = 0; i < lenJson; i++) {
			var nome = oJson.people[i].nome;
			console.log("Nome -> " + oJson.people[i].nome);
			param = "nome=" + oJson.people[i].nome      +
			 		"|idade=" + oJson.people[i].idade     +
			 		"|cpf=" + oJson.people[i].cpf       +
			 		"|rg=" + oJson.people[i].rg        +
			 		"|dtnsc=" + oJson.people[i].data_nasc +
			 		"|email=" + oJson.people[i].email     +
			 		"|cep=" + oJson.people[i].cep       +
			 		"|end=" + oJson.people[i].endereco  +
			 		"|numero=" + oJson.people[i].numero    +
			 		"|bairro=" + oJson.people[i].bairro    +
			 		"|cidade=" + oJson.people[i].cidade    +
			 		"|estado=" + oJson.people[i].estado    + "\n";
 			fs.appendFile('organizacao-do-json.txt', param, 'utf8', function () {});
		}
	    console.log("Arquivo salvo");
	});
});
