-- ============================================================
-- Exercícios de SQL: tabela vaga
-- ============================================================
-- Abra o vagas.db no DB Browser for SQLite (aba "Executar SQL")
-- ou no terminal: sqlite3 vagas.db
-- Antes, rode schema.sql e dados_exemplo.sql.

-- ---------- READ (SELECT) ----------

-- 1. Todas as vagas
SELECT * FROM vaga;

-- 2. Só algumas colunas
SELECT titulo, empresa FROM vaga;

-- 3. Filtro com WHERE
SELECT * FROM vaga WHERE empresa = 'Tech Campinas';

-- 4. Busca parcial com LIKE (% = qualquer texto)
SELECT * FROM vaga WHERE titulo LIKE '%DESENVOLVEDOR%';

-- 5. Ordenação
SELECT * FROM vaga ORDER BY titulo;
SELECT * FROM vaga ORDER BY titulo DESC;

-- 6. Contagem total
SELECT COUNT(*) AS total_vagas FROM vaga;

-- 7. Quantas vagas cada empresa oferece
SELECT empresa, COUNT(*) AS qtd
FROM vaga
GROUP BY empresa
ORDER BY qtd DESC;

-- ---------- CREATE (INSERT) ----------

-- 8. Nova vaga
INSERT INTO vaga (titulo, empresa, telefone) VALUES ('ESTÁGIO EM QA', 'Testes S.A.', '19 3666-8000');

-- 9. Tente inserir dados que violam o CHECK. O que acontece?
INSERT INTO vaga (titulo, empresa, telefone) VALUES ('VAGA', 'AB', '19 0000-0000');
INSERT INTO vaga (titulo, empresa, telefone) VALUES ('VAGA', 'Empresa', '11 0000-0000');

-- ---------- UPDATE ----------

-- 10. Alterar o telefone de uma vaga (sempre com WHERE!)
UPDATE vaga SET telefone = '19 9999-0000' WHERE id = 1;

-- 11. PERIGO: UPDATE sem WHERE altera TODAS as linhas.
--     Rode o SELECT antes para ver o que seria afetado:
-- SELECT * FROM vaga;
-- UPDATE vaga SET empresa = 'Ops';

-- ---------- DELETE ----------

-- 12. Remover uma vaga
DELETE FROM vaga WHERE id = 2;

-- 13. PERIGO: DELETE sem WHERE apaga a tabela inteira.
-- DELETE FROM vaga;

-- ---------- TRANSAÇÃO ----------

-- 14. Desfazer um erro com ROLLBACK
BEGIN;
DELETE FROM vaga;
SELECT COUNT(*) FROM vaga;   -- 0
ROLLBACK;
SELECT COUNT(*) FROM vaga;   -- os dados voltaram

-- ============================================================
-- DESAFIO: normalização e chave estrangeira
-- ============================================================
-- A empresa "Tech Campinas" aparece repetida em várias vagas.
-- a) Crie a tabela empresa (id, nome, telefone).
-- b) Crie a tabela vaga2 com a coluna empresa_id referenciando empresa(id):
--      empresa_id INTEGER NOT NULL REFERENCES empresa(id)
-- c) Ative as chaves estrangeiras: PRAGMA foreign_keys = ON;
-- d) Copie os dados de vaga para empresa e vaga2 (INSERT ... SELECT).
-- e) Liste as vagas com o nome da empresa usando JOIN.
-- f) Tente apagar uma empresa que ainda tem vagas. O que acontece?
