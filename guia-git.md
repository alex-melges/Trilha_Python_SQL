
# 📘 Guia de Fluxo de Trabalho com Git — Para não se confundir com branches

Este arquivo serve como um **guia prático para novatos** (como eu!) que estão começando a trabalhar com Git e GitHub em projetos com múltiplas branches. O objetivo é evitar confusão na hora de subir arquivos, criar novos módulos e garantir que tudo esteja sempre sincronizado com o repositório remoto.

---

## ✅ Fluxo Padrão de Trabalho com Branches

Sempre que for iniciar um novo módulo ou funcionalidade, siga **essa sequência de comandos**, explicados passo a passo:

---

### 1. Vá para a branch `master` e garanta que ela está atualizada
```bash
git checkout master
git pull origin master
```
- 🔄 **Explicação**: muda para a branch principal (`master`) e garante que ela está sincronizada com o GitHub.

---

### 2. Crie uma nova branch para o novo módulo
```bash
git checkout -b modulo-xy
```
- 🌱 **Explicação**: cria e já muda para a nova branch (`modulo-04`), baseada na master atualizada.

---

### 3. Trabalhe normalmente no projeto
- Crie arquivos, edite scripts, atualize o `README.md`.
- Sempre que terminar uma parte, faça:
```bash
git add .
git commit -m "mensagem explicando o que foi feito"
```
- 💡 **Dica**: evite deixar arquivos “Untracked”. Use `git status` para conferir.

---

### 4. Suba sua branch para o GitHub
```bash
git push origin modulo-xy
```
- ☁️ **Explicação**: envia sua nova branch (e os commits) para o GitHub.

---

### 5. Crie um Pull Request (PR)
- Acesse o repositório no GitHub.
- Clique em “Compare & Pull Request”.
- Adicione uma descrição e crie o PR.
- Faça o merge no GitHub e depois **delete a branch remota** se quiser.

---

### 6. Volte à master e atualize localmente
```bash
git checkout master
git pull origin master
```
- ✅ **Explicação**: isso garante que sua master local está com o merge feito no GitHub.

---

### 7. Crie uma tag para marcar o fim do módulo
```bash
git tag modulo-xy-finalizado
git push origin modulo-xy
```
- 🏷️ **Explicação**: cria uma “etiqueta” no repositório marcando o fim do módulo, útil para consultar depois.

---

## 🔁 Resumo do Fluxo

```bash
git checkout master
git pull origin master
git checkout -b modulo-xy

# Trabalha e comita...

git push origin modulo-xy
# (faz o merge no GitHub)

git checkout master
git pull origin master
git tag modulo-xy-finalizado
git push origin modulo-XX
```

---

Seguindo essa ordem, você evita erros comuns como arquivos faltando, branches desatualizadas ou conflitos inesperados.
