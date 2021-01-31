![Screenshot_2021-01-31 TryHackMe Vulnversity](https://user-images.githubusercontent.com/51774020/106397964-ee851f00-63ee-11eb-8818-208d93094e20.png)

Ao conectar na máquina iremos utilizar o nmap para descobrir as portas de rede que estão abertas. Verificando o resultado, vemos que esta máquina possui 6 portas de rede aberta.

![Screenshot from 2021-01-31 17-36-45](https://user-images.githubusercontent.com/51774020/106398044-73703880-63ef-11eb-9af1-bbd950ed1df1.png)

utilizando o dirb (localizador de diretórias a partir de uma wordlist) identificamos um deretório chamado "internal" onde podemos incluir arquivos.

![Screenshot from 2021-01-31 17-38-28](https://user-images.githubusercontent.com/51774020/106398277-b1219100-63f0-11eb-8521-c7b7e32965c6.png)

Pesquisando um pouco mais, vemos que podemos incluir uma shell-reverse nesse input de dados.Realizando essa inclusão com sucesso, encontramos o diretório "Uploads".

![Screenshot from 2021-01-31 17-39-04](https://user-images.githubusercontent.com/51774020/106398330-f34ad280-63f0-11eb-9a45-a93cfcdbcc95.png)

Configurando o NetCat para realizar a conexão reversa, observamos que conseguimos acesso a uma shell no servidor. Logo após entrar no diretório "/home/bill/user.txt" conseguimos a primeira flag. 

![Screenshot from 2021-01-31 17-47-43](https://user-images.githubusercontent.com/51774020/106398410-5dfc0e00-63f1-11eb-827a-a3e4bd9d602e.png)
![Screenshot from 2021-01-31 17-48-43](https://user-images.githubusercontent.com/51774020/106398412-60f6fe80-63f1-11eb-8a72-a0f2b23082bf.png)
![Screenshot from 2021-01-31 17-51-54](https://user-images.githubusercontent.com/51774020/106398413-63595880-63f1-11eb-9500-bd3f833572e8.png)

Utilizando o comando " cd /bin" iremos para o diretório /bin. Com isso, utilizando o comando "find -perm -4000" vemos que temos acesso ao arquivo "systemclt". Sendo assim conseguimos a flag root.

```
TF=$(mktemp).service
echo '[Service]
Type=oneshot
ExecStart=/bin/sh -c "id > /tmp/output"
[Install]
WantedBy=multi-user.target' > $TF
./systemctl link $TF
./systemctl enable --now $TF

```
![Screenshot from 2021-01-31 17-57-52](https://user-images.githubusercontent.com/51774020/106398434-82f08100-63f1-11eb-83fc-e4ae74d1c1d1.png)

![Screenshot from 2021-01-31 17-58-16](https://user-images.githubusercontent.com/51774020/106398436-83891780-63f1-11eb-90c3-fa4b241281c6.png)
