
-- jogos definition

CREATE TABLE jogos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    data TEXT NOT NULL,
    nota INTEGER NOT NULL, 
    link TEXT NOT NULL
);


INSERT INTO jogos (title,"data",content,nota,link) VALUES
	 ('Call of Duty®: Black Ops III','06/10/2015','Call of Duty®: Black Ops III Edição Zombies Chronicles inclui o jogo base completo e o conteúdo da expansão Zombies Chronicles.','7.5','https://store.steampowered.com/app/311210/Call_of_Duty_Black_Ops_III/'),
	 ('Crash Bandicoot™ N. Sane Trilogy','29/06/2018','Seu marsupial favorito, Crash Bandicoot®, voltou! Aprimorado, inspirado e pronto para dançar nessa trilogia insana. Reviva seus momentos favoritos em Crash Bandicoot™, Crash Bandicoot™ 2: Cortex Strikes Back e Crash Bandicoot™ 3: Warped, agora com gráficos HD completamente remasterizados!','7.83333333333333','https://store.steampowered.com/app/731490/Crash_Bandicoot_N_Sane_Trilogy/'),
	 ('Zeus + Poseidon','15/12/2016','Zeus + Poseidon delivers hundreds of hours of gameplay in one game!','8.33333333333333','https://store.steampowered.com/app/566050/Zeus__Poseidon/'),
	 ('ELDEN RING','24/02/2022','O NOVO RPG DE AÇÃO E FANTASIA. Levante-se, Maculado, e seja guiado pela graça para portar o poder do Anel Prístino e se tornar um Lorde Prístino nas Terras Intermédias.','9.33333333333333','https://store.steampowered.com/app/1245620/ELDEN_RING/'),
	 ('DARK SOULS: REMASTERED','23/05/2018','Mas então, fez-se o fogo. Experimente novamente o jogo aclamado pela crítica e definidor de gênero que foi o início tudo. Belamente remasterizado, volte a Lordran com detalhes em alta definição a 60fps.','6.83333333333333','https://store.steampowered.com/app/570940/DARK_SOULS_REMASTERED/?curator_clanid=33042543'),
	 ('NARUTO SHIPPUDEN: Ultimate Ninja STORM 4','04/02/2016','O mais recente capítulo da aclamada série STORM leva você a uma viagem de tirar o fôlego e cheia de cores! Tire proveito do sistema de batalha totalmente renovado e prepare-se para mergulhar nas lutas mais épicas que você já viu!','7.0','https://store.steampowered.com/app/349040/NARUTO_SHIPPUDEN_Ultimate_Ninja_STORM_4/'),
	 ('LEGO® Star Wars™: A Saga Skywalker','05/04/2022','Jogue em todos os nove filmes da saga Skywalker em um jogo diferente de qualquer outro. Com mais de 300 personagens jogáveis, mais de 100 veículos e 23 planetas para explorar, uma galáxia muito, muito distante nunca foi tão divertida! *Inclui o personagem jogável Obi-Wan Kenobi Clássico','8.5','https://store.steampowered.com/app/920210/LEGO_Star_Wars_A_Saga_Skywalker/'),
	 ('LEGO® The Incredibles','15/06/2018','Viva as aventuras eletrizantes da família Parr na luta contra o crime e por uma vida mais caseira nos dois filmes de longa-metragem da Disney-Pixar, Os Incríveis e Os Incríveis 2, em um mundo LEGO® cheio de diversão e humor.','8.0','https://store.steampowered.com/app/818320/LEGO_The_Incredibles/'),
	 ('LEGO® Batman™ 3: Beyond Gotham','11/11/2014','The Caped Crusader joins forces with the super heroes of the DC Comics universe and blasts off to outer space to stop the evil Brainiac from destroying Earth.','7.5','https://store.steampowered.com/app/313690/LEGO_Batman_3_Beyond_Gotham/'),
	 ('Cuphead','29/09/2017','Cuphead é um jogo de ação e tiros clássico, com enorme ênfase nas batalhas de chefes. Inspirado nas animações infantis da década de 1930, os visuais e efeitos sonoros foram minuciosamente recriados com as mesmíssimas técnicas dessa era, com destaque para desenhos feitos à mão, fundos em aquarela e gravações originais de jazz.','8.83333333333333','https://store.steampowered.com/app/268910/Cuphead/');
INSERT INTO jogos (title,"data",content,nota,link) VALUES
	 ('Stardew Valley','26/02/2016','Você herdou a antiga fazenda do seu avô, em Stardew Valley. Com ferramentas de segunda-mão e algumas moedas, você parte para dar início a sua nova vida. Será que você vai aprender a viver da terra, a transformar esse matagal em um próspero lar?','8.0','https://store.steampowered.com/app/413150/Stardew_Valley/'),
	 ('Dota Underlords','20/06/2019','Contrate um exército e destrua seus rivais no novo jogo no mundo do Dota. Apresentando a 1ª temporada: explore a Espiral Branca e ganhe recompensas no passe de batalha. Com vários modos diferentes, jogue sozinho ou com amigos e sincronize o progresso no PC e no celular.','6.33333333333333','https://store.steampowered.com/app/1046930/Dota_Underlords/'),
	 ('Portal 2','19/04/2011','The "Perpetual Testing Initiative" has been expanded to allow you to design co-op puzzles for you and your friends!','9.5','https://store.steampowered.com/app/620/Portal_2/'),
	 ('Half-Life 2: Episode Two','10/10/2007','Half-Life® 2: Episode Two é o segundo jogo de uma nova trilogia criada pela Valve que estende a aventura premiada e sucesso de vendas de Half-Life®.

Como o Dr. Gordon Freeman, você foi visto pela última vez saindo da Cidade 17 com Alyx Vance enquanto a Fortaleza entrava em erupção no meio de uma tempestade de proporções desconhecidas. Em Episode Two, você deve lutar e correr contra forças Combine enquanto você atravessa a Floresta Branca para entregar um pacote de dados crucial, roubado da Fortaleza para um grupo de resistência de colegas cientistas.

Episode Two estende a premiada jogabilidade de Half-Life com armas e veículos únicos, além de criaturas inéditas.','9.66666666666667','https://store.steampowered.com/app/420/HalfLife_2_Episode_Two/'),
	 ('Dota 2','09/07/2013','Diariamente, milhões de jogadores mundo afora batalham como um dentre os mais de cem heróis do Dota. Estejam jogando há 10 ou 1.000 horas, há sempre algo novo para descobrir. Com atualizações constantes das mecânicas, recursos e heróis, o Dota 2 se tornou mais que um simples jogo.','5.0','https://store.steampowered.com/app/570/Dota_2/');