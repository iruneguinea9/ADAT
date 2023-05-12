delimiter $$
create or replace function insertar_nota_irune(cod int,dni varchar2,nota int) return varchar2 is 
    estaba number(1);
    vuelta varchar2(20);
    begin 
        select count(*) into estaba from examen2.notas where notas.dni = dni and notas.cod = cod;
        if(estaba=0) THEN -- es que no estaba, añadimos
            insert into examen2.notas values (cod,dni,nota);
            vuelta = 'Nota creada correctamente' ;
        else
            -- modificar
            update examen2.notas set notas.nota = nota where notas.dni= dni and notas.cod = cod;
            vuelta = 'Nota modificada correctamente';
        end if;
    return vuelta;
end parte4_Irune$$
delimiter;
