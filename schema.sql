-- ============================================================
-- Estrutura do banco de vagas de estágio (SQLite)
-- ============================================================
-- As mesmas regras do formulário Django (estagios/core/forms.py)
-- aparecem aqui como restrições do próprio banco:
--   * empresa precisa ter ao menos 3 caracteres
--   * telefone precisa começar com o DDD 19
-- Assim, nem a aplicação consegue gravar um dado inválido.

CREATE TABLE IF NOT EXISTS vaga (
    -- Chave primária: o SQLite gera o número automaticamente
    id       INTEGER PRIMARY KEY AUTOINCREMENT,

    -- NOT NULL: o campo é obrigatório
    titulo   TEXT NOT NULL,

    -- CHECK: condição que todo registro precisa satisfazer
    empresa  TEXT NOT NULL CHECK (length(empresa) >= 3),

    telefone TEXT NOT NULL CHECK (telefone LIKE '19%')
);
