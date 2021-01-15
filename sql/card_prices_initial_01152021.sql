-- NOTE: ran on development 1/15/21 LK
CREATE TABLE IF NOT EXISTS card_prices (
  sku integer not null primary key,
  low numeric(5,2),
  market numeric(5,2),
  direct numeric(5,2),
  bl_high numeric(5,2),
  created_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP NOT NULL
)