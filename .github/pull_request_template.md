<!--
Pull request вливается через squash, поэтому заголовок пишется по Conventional Commits:
`fix: ...`, `feat: ...`, `docs: ...`, `refactor: ...`, `test: ...`, `chore: ...`.
-->

## Описание

<!-- Что меняется и зачем? -->

## Связанные задачи

<!-- `Closes #123` закроет задачу при слиянии. Если задач нет, удалите этот раздел. -->

## Проверка

<!-- Как вы убедились, что всё работает? -->

## Чек-лист

- [ ] `uvx prek run --all-files` проходит.
- [ ] Описания полей указывают единицы измерения, если их не видно из названия, и совпадают со спецификацией Gismeteo API v2.
- [ ] [pygismeteo](https://github.com/monosans/pygismeteo) и [aiopygismeteo](https://github.com/monosans/aiopygismeteo) работают с этим изменением.
