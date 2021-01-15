CREATE TABLE IF NOT EXISTS card_prices (
  sku INTEGER not null primary key,

  bl_high NUMERIC(5,2),
  direct NUMERIC(5,2),
  low NUMERIC(5,2),
  market NUMERIC(5,2),

  created_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP NOT NULL
)