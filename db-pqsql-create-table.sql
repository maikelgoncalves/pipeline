CREATE TABLE IF NOT EXISTS vendas (
	id SERIAL PRIMARY KEY,
	email varchar(255) not null,
	data timestamp not null,
	valor numeric not null,
	qtde integer not null,
	produto varchar(64) not null
)