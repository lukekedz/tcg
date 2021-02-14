CREATE TABLE IF NOT EXISTS card_prices (
  bl_high NUMERIC(10,2),
  direct NUMERIC(10,2),
  low NUMERIC(10,2),
  market NUMERIC(10,2),

  created_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP NOT NULL,

  sku INTEGER NOT NULL,
  cpkey VARCHAR(20),
  PRIMARY KEY(created_at, sku)
)