# Diplom
Итоговый проект.
Комментрий к Спринт2:
1. Для всех текстовых полей использовал тип text, т.к. на Postgres/Greenplam использование text\varchar практически не отличается от скорости обработки varchar(N), а в некотрых случаях быстрее чем varchar(N).
2. Для подключения использую файл "...\Application Data\postgresql\.pg_service.conf" в котром описан my_service
3. В сервис AWS S3 не удалось зарегистрироваться из-за санкционных ограницений (нет действующей карты VISA/Mastercard)
4. Про поиск не понял что именно нужно реализовать. Реализовал поиск по модели Clips с помощью Q.
5. Подключил авторизацию для Google.

P.S.
Если я что-то не понял или реализовал не так напишите, пожалуйста, в Slack - исправлю.
Спасибо.