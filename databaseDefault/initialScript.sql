/*------------------------------------------------------------------------------------------------------------------------------------*/
/*_______________________________________CEO__________________________________________________________________________________________*/
/*------------------------------------------------------------------------------------------------------------------------------------*/

insert into usuarios_administradorduenio values (DEFAULT, 'Marthox', md5('1234'), 'CEO');

/*------------------------------------------------------------------------------------------------------------------------------------*/
/*_______________________________________ADMIN________________________________________________________________________________________*/
/*------------------------------------------------------------------------------------------------------------------------------------*/

insert into usuarios_administradorduenio values (DEFAULT, 'Valeria', md5('1234'), 'ADMIN');
insert into usuarios_administradorduenio values (DEFAULT, 'Emily', md5('1234'), 'ADMIN');

/*------------------------------------------------------------------------------------------------------------------------------------*/
/*_______________________________________CLIENTE______________________________________________________________________________________*/
/*------------------------------------------------------------------------------------------------------------------------------------*/

insert into usuarios_cliente values ('Felipe', md5('1234'), DATE '1999/07/12', '15539 Forster Trail', '5003821077', 'CC', '307540');
insert into usuarios_cliente values ('Jaime', md5('1234'), DATE '1998/12/28', '15539 Forster Trail', '5003821077', 'CC', '307540');
insert into usuarios_cliente values ('Sara', md5('1234'), DATE '2001/01/04', '15539 Forster Trail', '5003821077', 'CC', '307540');
insert into usuarios_cliente values ('Natalia', md5('1234'), DATE '2001/07/23', '15539 Forster Trail', '5003821077', 'CC', '307540');
insert into usuarios_cliente values ('Maria Jose', md5('1234'), DATE '2001/05/25', '15539 Forster Trail', '5003821077', 'CC', '307540');
insert into usuarios_cliente values ('Camila', md5('1234'), DATE '2002/04/12', '15539 Forster Trail', '5003821077', 'CC', '307540');
insert into usuarios_cliente values ('Laura', md5('1234'), DATE '1991/08/05', '15539 Forster Trail', '5003821077', 'CC', '307540');
insert into usuarios_cliente values ('Marcela', md5('1234'), DATE '1995/06/03', '15539 Forster Trail', '5003821077', 'CC', '307540');

/*------------------------------------------------------------------------------------------------------------------------------------*/
/*_______________________________________PROVEEDOR____________________________________________________________________________________*/
/*------------------------------------------------------------------------------------------------------------------------------------*/

insert into inventario_proveedor values ('8367329046293', '2371 Golf Circle', '7580506150');
insert into inventario_proveedor values ('0334242915368', '2022 Sommers Place', '4219896872');

/*------------------------------------------------------------------------------------------------------------------------------------*/
/*_______________________________________BODEGA_______________________________________________________________________________________*/
/*------------------------------------------------------------------------------------------------------------------------------------*/

insert into inventario_bodega values (DEFAULT, '2344 Street Charles', 'CALI');
insert into inventario_bodega values (DEFAULT, '4560 Street Valeria', 'CALI');

/*------------------------------------------------------------------------------------------------------------------------------------*/
/*_______________________________________CATEGORIA____________________________________________________________________________________*/
/*------------------------------------------------------------------------------------------------------------------------------------*/

insert into inventario_categoria values (DEFAULT, 'Hombres', '../media/categoriasImagenes/categorias.jpg'); /* id_categoria: 1*/
insert into inventario_categoria values (DEFAULT, 'Mujeres', '../media/categoriasImagenes/categorias.jpg'); /* id_categoria: 2*/
insert into inventario_categoria values (DEFAULT, 'Niños', '../media/categoriasImagenes/categorias.jpg'); /* id_categoria: 3*/
insert into inventario_categoria values (DEFAULT, 'Accesorios', '../media/categoriasImagenes/categorias.jpg'); /* id_categoria: 4*/
insert into inventario_categoria values (DEFAULT, 'Zapatos', '../media/categoriasImagenes/categorias.jpg'); /* id_categoria: 5*/

/*------------------------------------------------------------------------------------------------------------------------------------*/
/*_______________________________________SUBCATEGORIA_________________________________________________________________________________*/
/*------------------------------------------------------------------------------------------------------------------------------------*/

insert into inventario_subcategoria values (DEFAULT, 'CamisetasH', 1); /* id_subcategoria: 1*/
insert into inventario_subcategoria values (DEFAULT, 'CamisasH', 1); /* id_subcategoria: 2*/
insert into inventario_subcategoria values (DEFAULT, 'PantalonesH', 1); /* id_subcategoria: 3*/
insert into inventario_subcategoria values (DEFAULT, 'CamisetasM', 2); /* id_subcategoria: 4*/
insert into inventario_subcategoria values (DEFAULT, 'FaldasM', 2); /* id_subcategoria: 5*/
insert into inventario_subcategoria values (DEFAULT, 'VestidosM', 2); /* id_subcategoria: 6*/
insert into inventario_subcategoria values (DEFAULT, 'Pijamas', 3); /* id_subcategoria: 7*/
insert into inventario_subcategoria values (DEFAULT, 'VestidosNiña', 3); /* id_subcategoria: 8*/
insert into inventario_subcategoria values (DEFAULT, 'Chaquetas', 3); /* id_subcategoria: 9*/
insert into inventario_subcategoria values (DEFAULT, 'Bolsos', 4); /* id_subcategoria: 10*/
insert into inventario_subcategoria values (DEFAULT, 'Correas', 4); /* id_subcategoria: 11*/
insert into inventario_subcategoria values (DEFAULT, 'Gorros', 4); /* id_subcategoria: 12*/
insert into inventario_subcategoria values (DEFAULT, 'ZapatosHombre', 5); /* id_subcategoria: 13*/
insert into inventario_subcategoria values (DEFAULT, 'ZapatosMujer', 5); /* id_subcategoria: 14*/

/*------------------------------------------------------------------------------------------------------------------------------------*/
/*_______________________________________CAMISETAS____________________________________________________________________________________*/
/*------------------------------------------------------------------------------------------------------------------------------------*/

insert into inventario_producto values (DEFAULT,'Camiseta1','descripcion1', 19, 23000, '../media/productosImagenes/Camiseta1.jpg', 1); /* id_producto: 1*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,1,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'S','gris',20,1,1,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'L','blanco',20,1,1,'8367329046293');

insert into inventario_producto values (DEFAULT,'Camiseta2','descripcion2', 19, 23000, '../media/productosImagenes/Camiseta2.jpg', 1); /* id_producto: 2*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,2,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'S','negro',20,1,2,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'L','blanco',20,1,2,'0334242915368');

insert into inventario_producto values (DEFAULT,'Camiseta3','descripcion3', 19,23000, '../media/productosImagenes/Camiseta3.jpg', 1); /* id_producto: 3*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,3,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'S','gris',20,1,3,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'L','blanco',20,1,3,'8367329046293');

insert into inventario_producto values (DEFAULT,'Camiseta4','descripcion4', 19, 23000, '../media/productosImagenes/Camiseta4.jpg', 1); /* id_producto: 4*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,4,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'S','negro',20,1,4,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'L','blanco',20,1,4,'0334242915368');

/*------------------------------------------------------------------------------------------------------------------------------------*/
/*_______________________________________CAMISAS______________________________________________________________________________________*/
/*------------------------------------------------------------------------------------------------------------------------------------*/

insert into inventario_producto values (DEFAULT,'Camisa1','descripcion1', 19, 23000, '../media/productosImagenes/Camisa1.jpg', 2);  /* id_producto: 5*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,5,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'S','gris',20,1,5,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'L','blanco',20,1,5,'8367329046293');

insert into inventario_producto values (DEFAULT,'Camisa2','descripcion2', 19, 23000, '../media/productosImagenes/Camisa2.jpg', 2); /* id_producto: 6*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,6,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'S','negro',20,1,6,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'L','blanco',20,1,6,'0334242915368');

insert into inventario_producto values (DEFAULT,'Camisa3','descripcion3', 19, 23000, '../media/productosImagenes/Camisa3.jpg', 2); /* id_producto: 7*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,7,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'S','gris',20,1,7,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'L','blanco',20,1,7,'8367329046293');

insert into inventario_producto values (DEFAULT,'Camisa4','descripcion4', 19, 23000, '../media/productosImagenes/Camisa4.jpg', 2); /* id_producto: 8*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,8,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'XS','negro',20,1,8,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'L','blanco',20,1,8,'0334242915368');

/*------------------------------------------------------------------------------------------------------------------------------------*/
/*_______________________________________PANTALONES___________________________________________________________________________________*/
/*------------------------------------------------------------------------------------------------------------------------------------*/

insert into inventario_producto values (DEFAULT,'Pantalon1','descripcion1', 19,23000, '../media/productosImagenes/Pantalon1.jpg', 3);  /* id_producto: 9*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,9,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'SL','gris',20,1,9,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'L','blanco',20,1,9,'8367329046293');

insert into inventario_producto values (DEFAULT,'Pantalon2','descripcion2', 19,23000, '../media/productosImagenes/Pantalon2.jpg', 3); /* id_producto: 10*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,10,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'SL','negro',20,1,10,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'L','blanco',20,1,10,'0334242915368');

insert into inventario_producto values (DEFAULT,'Pantalon3','descripcion3', 19,23000, '../media/productosImagenes/Pantalon3.jpg', 3); /* id_producto: 11*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,11,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'SL','gris',20,1,11,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'L','blanco',20,1,11,'8367329046293');

insert into inventario_producto values (DEFAULT,'Pantalon4','descripcion4', 19,23000, '../media/productosImagenes/Pantalon4.jpg', 3); /* id_producto: 12*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,12,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'SL','negro',20,1,12,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'L','blanco',20,1,12,'0334242915368');

/*------------------------------------------------------------------------------------------------------------------------------------*/
/*_______________________________________BLUSAS_______________________________________________________________________________________*/
/*------------------------------------------------------------------------------------------------------------------------------------*/

insert into inventario_producto values (DEFAULT,'Blusa1','descripcion1', 19,23000, '../media/productosImagenes/Blusa1.jpg', 4); /* id_producto: 13*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,13,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'SL','gris',20,1,13,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'L','blanco',20,1,13,'8367329046293');

insert into inventario_producto values (DEFAULT,'Blusa2','descripcion2', 19,23000, '../media/productosImagenes/Blusa2.jpg', 4); /* id_producto: 14*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,14,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'S','negro',20,1,14,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'M','blanco',20,1,14,'0334242915368');

insert into inventario_producto values (DEFAULT,'Blusa3','descripcion3', 19,23000, '../media/productosImagenes/Blusa3.jpg', 4); /* id_producto: 15*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,15,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'S','gris',20,1,15,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'L','blanco',20,1,15,'8367329046293');

insert into inventario_producto values (DEFAULT,'Blusa4','descripcion4', 19,23000, '../media/productosImagenes/Blusa4.jpg', 4); /* id_producto: 16*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,16,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'S','negro',20,1,16,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'M','blanco',20,1,16,'0334242915368');

insert into inventario_producto values (DEFAULT,'Blusa5','descripcion5', 19,23000, '../media/productosImagenes/Blusa5.jpg', 4); /* id_producto: 17*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,17,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'SL','gris',20,1,17,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'L','blanco',20,1,17,'8367329046293');

insert into inventario_producto values (DEFAULT,'Blusa6','descripcion6', 19,23000, '../media/productosImagenes/Blusa6.jpg', 4); /* id_producto: 18*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,18,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'S','negro',20,1,18,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'M','blanco',20,1,18,'0334242915368');

insert into inventario_producto values (DEFAULT,'Blusa7','descripcion7', 19,23000, '../media/productosImagenes/Blusa7.jpg', 4); /* id_producto: 19*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,19,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'S','gris',20,1,19,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'L','blanco',20,1,19,'8367329046293');

insert into inventario_producto values (DEFAULT,'Blusa8','descripcion8', 19,23000, '../media/productosImagenes/Blusa8.jpg', 4); /* id_producto: 20*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,20,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'S','negro',20,1,20,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'M','blanco',20,1,20,'0334242915368');

/*------------------------------------------------------------------------------------------------------------------------------------*/
/*_______________________________________FALDAS_______________________________________________________________________________________*/
/*------------------------------------------------------------------------------------------------------------------------------------*/

insert into inventario_producto values (DEFAULT,'Falda1','descripcion1', 19,23000, '../media/productosImagenes/Falda1.jpg', 5); /** id_producto: 21*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,21,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'S','gris',20,1,21,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'L','blanco',20,1,21,'8367329046293');

insert into inventario_producto values (DEFAULT,'Falda2','descripcion2', 19,23000, '../media/productosImagenes/Falda2.jpg', 5); /** id_producto: 22*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,22,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'S','negro',20,1,22,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'M','blanco',20,1,22,'0334242915368');

insert into inventario_producto values (DEFAULT,'Falda3','descripcion3', 19,23000, '../media/productosImagenes/Falda3.jpg', 5); /** id_producto: 23*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,23,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'S','gris',20,1,23,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'L','blanco',20,1,23,'8367329046293');

insert into inventario_producto values (DEFAULT,'Falda4','descripcion4', 19,23000, '../media/productosImagenes/Falda4.jpg', 5); /** id_producto: 24*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,24,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'S','negro',20,1,24,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'M','blanco',20,1,24,'0334242915368');

/*------------------------------------------------------------------------------------------------------------------------------------*/
/*_______________________________________VESTIDOS_____________________________________________________________________________________*/
/*------------------------------------------------------------------------------------------------------------------------------------*/

insert into inventario_producto values (DEFAULT,'Vestido1','descripcion1', 19,23000, '../media/productosImagenes/Vestido1.jpg', 6); /** id_producto: 25*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,25,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'S','gris',20,1,25,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'L','blanco',20,1,25,'8367329046293');

insert into inventario_producto values (DEFAULT,'Vestido2','descripcion2', 19,23000, '../media/productosImagenes/Vestido2.jpg', 6); /** id_producto: 26*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,26,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'S','negro',20,1,26,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'M','blanco',20,1,26,'0334242915368');

insert into inventario_producto values (DEFAULT,'Vestido3','descripcion3', 19,23000, '../media/productosImagenes/Vestido3.jpg', 6); /** id_producto: 27*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,27,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'S','gris',20,1,27,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'L','blanco',20,1,27,'8367329046293');

insert into inventario_producto values (DEFAULT,'Vestido4','descripcion4', 19,23000, '../media/productosImagenes/Vestido4.jpg', 6); /** id_producto: 28*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,28,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'S','negro',20,1,28,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'M','blanco',20,1,28,'0334242915368');

/*------------------------------------------------------------------------------------------------------------------------------------*/
/*_______________________________________ZAPATOS HOMBRE_______________________________________________________________________________*/
/*------------------------------------------------------------------------------------------------------------------------------------*/

insert into inventario_producto values (DEFAULT,'ZapatosHombre1','descripcion1', 19,23000, '../media/productosImagenes/ZapatosHombre1.jpg', 13); /** id_producto: 29*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,29,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'S','gris',20,1,29,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'L','blanco',20,1,29,'8367329046293');

insert into inventario_producto values (DEFAULT,'ZapatosHombre2','descripcion2', 19,23000, '../media/productosImagenes/ZapatosHombre2.jpg', 13); /** id_producto: 30*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,30,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'S','negro',20,1,30,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'M','blanco',20,1,30,'0334242915368');

insert into inventario_producto values (DEFAULT,'ZapatosHombre3','descripcion3', 19,23000, '../media/productosImagenes/ZapatosHombre3.jpg', 13); /** id_producto: 31*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,31,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'S','gris',20,1,31,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'L','blanco',20,1,31,'8367329046293');

insert into inventario_producto values (DEFAULT,'ZapatosHombre4','descripcion4', 19,23000, '../media/productosImagenes/ZapatosHombre4.jpg', 13); /** id_producto: 32*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,32,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'S','negro',20,1,32,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'M','blanco',20,1,32,'0334242915368');

/*------------------------------------------------------------------------------------------------------------------------------------*/
/*_______________________________________ZAPATOS MUJER________________________________________________________________________________*/
/*------------------------------------------------------------------------------------------------------------------------------------*/

insert into inventario_producto values (DEFAULT,'ZapatosMujer1','descripcion1', 19,23000, '../media/productosImagenes/ZapatosMujer1.jpg', 14); /** id_producto: 33*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,33,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'S','gris',20,1,33,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'L','blanco',20,1,33,'8367329046293');

insert into inventario_producto values (DEFAULT,'ZapatosMujer2','descripcion2', 19,23000, '../media/productosImagenes/ZapatosMujer2.jpg', 14); /** id_producto: 34*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,34,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'S','negro',20,1,34,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'M','blanco',20,1,34,'0334242915368');

insert into inventario_producto values (DEFAULT,'ZapatosMujer3','descripcion3', 19,23000, '../media/productosImagenes/ZapatosMujer3.jpg', 14); /** id_producto: 35*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,35,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'S','gris',20,1,35,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'L','blanco',20,1,35,'8367329046293');

insert into inventario_producto values (DEFAULT,'ZapatosMujer4','descripcion4', 19,23000, '../media/productosImagenes/ZapatosMujer4.jpg', 14); /** id_producto: 36*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,36,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'S','negro',20,1,36,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'M','blanco',20,1,36,'0334242915368');

/*------------------------------------------------------------------------------------------------------------------------------------*/
/*_______________________________________CAMISETAS-2____________________________________________________________________________________*/
/*------------------------------------------------------------------------------------------------------------------------------------*/

insert into inventario_producto values (DEFAULT,'Camiseta1','descripcion1', 19, 23000, '../media/productosImagenes/Camiseta5.jpg', 1); /* id_producto: 37*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,37,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'S','gris',20,1,37,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'L','blanco',20,1,37,'8367329046293');

insert into inventario_producto values (DEFAULT,'Camiseta2','descripcion2', 19, 23000, '../media/productosImagenes/Camiseta6.jpg', 1); /* id_producto: 38*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,38,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'S','negro',20,1,38,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'L','blanco',20,1,38,'0334242915368');

insert into inventario_producto values (DEFAULT,'Camiseta3','descripcion3', 19,23000, '../media/productosImagenes/Camiseta7.jpg', 1); /* id_producto: 38*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,39,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'S','gris',20,1,39,'8367329046293');
insert into inventario_detallesproducto values (DEFAULT, 'L','blanco',20,1,39,'8367329046293');

insert into inventario_producto values (DEFAULT,'Camiseta4','descripcion4', 19, 23000, '../media/productosImagenes/Camiseta8.jpg', 1); /* id_producto: 40*/
insert into inventario_detallesproducto values (DEFAULT, 'XS','morado',20,1,40,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'S','negro',20,1,40,'0334242915368');
insert into inventario_detallesproducto values (DEFAULT, 'L','blanco',20,1,40,'0334242915368');

/*------------------------------------------------------------------------------------------------------------------------------------*/
/*_______________________________________DESCUENTOS PRODUCTO__________________________________________________________________________*/
/*------------------------------------------------------------------------------------------------------------------------------------*/

insert into ventas_descuentoproducto values (DEFAULT, DATE '2019/08/17',DATE '2019/08/20',3,15);
insert into ventas_descuentoproducto values (DEFAULT, DATE '2019/08/17',DATE '2019/08/20',3,30);
insert into ventas_descuentoproducto values (DEFAULT, DATE '2016/08/17',DATE '2017/08/19',99,15);
insert into ventas_descuentoproducto values (DEFAULT, DATE '2016/08/17',DATE '2017/08/19',99,30);

/*------------------------------------------------------------------------------------------------------------------------------------*/
/*_______________________________________DESCUENTOS CATEGORIA_________________________________________________________________________*/
/*------------------------------------------------------------------------------------------------------------------------------------*/

insert into ventas_descuentocategoria values (DEFAULT, DATE '2019/07/17',DATE '2019/08/20',15,2);
insert into ventas_descuentocategoria values (DEFAULT, DATE '2019/07/17',DATE '2019/08/20',15,2);
insert into ventas_descuentocategoria values (DEFAULT, DATE '2019/07/17',DATE '2019/08/20',15,2);
insert into ventas_descuentocategoria values (DEFAULT, DATE '2019/07/17',DATE '2019/08/20',2,1);
insert into ventas_descuentocategoria values (DEFAULT, DATE '2016/07/17',DATE '2017/07/18',99,2);
insert into ventas_descuentocategoria values (DEFAULT, DATE '2016/07/17',DATE '2017/08/20',99,2);
insert into ventas_descuentocategoria values (DEFAULT, DATE '2016/07/17',DATE '2017/07/18',99,1);
insert into ventas_descuentocategoria values (DEFAULT, DATE '2016/07/17',DATE '2017/08/20',99,2);

/*------------------------------------------------------------------------------------------------------------------------------------*/
/*_______________________________________DESCUENTOS SUBCATEGORIA______________________________________________________________________*/
/*------------------------------------------------------------------------------------------------------------------------------------*/

insert into ventas_descuentosubcategoria values (DEFAULT, DATE '2019/07/17',DATE '2019/08/20',1,6);
insert into ventas_descuentosubcategoria values (DEFAULT, DATE '2019/07/17',DATE '2019/08/20',2,4);
insert into ventas_descuentosubcategoria values (DEFAULT, DATE '2019/07/17',DATE '2019/08/20',3,2);
insert into ventas_descuentosubcategoria values (DEFAULT, DATE '2019/07/17',DATE '2019/08/20',15,3);
insert into ventas_descuentosubcategoria values (DEFAULT, DATE '2019/07/17',DATE '2019/08/20',2,13);
insert into ventas_descuentosubcategoria values (DEFAULT, DATE '2016/07/17',DATE '2017/07/18',99,5);
insert into ventas_descuentosubcategoria values (DEFAULT, DATE '2016/07/17',DATE '2017/07/18',99,6);
insert into ventas_descuentosubcategoria values (DEFAULT, DATE '2016/07/17',DATE '2017/07/18',99,4);
insert into ventas_descuentosubcategoria values (DEFAULT, DATE '2016/07/17',DATE '2017/07/18',99,2);
insert into ventas_descuentosubcategoria values (DEFAULT, DATE '2016/07/17',DATE '2017/08/20',99,3);
insert into ventas_descuentosubcategoria values (DEFAULT, DATE '2016/07/17',DATE '2017/07/18',99,13);

/*------------------------------------------------------------------------------------------------------------------------------------*/
/*_______________________________________SHOOOOOPIIIIINGGGGGGGGGGG____________________________________________________________________*/
/*------------------------------------------------------------------------------------------------------------------------------------*/

insert into ventas_factura values (DEFAULT, DATE '2019/07/01', 'Felipe');  /** id_factura: 1*/
insert into ventas_pagoscredito values (DEFAULT, '1234', DATE '2019/07/01', 'A', 100, 1);
insert into ventas_detallesfactura values (DEFAULT, 2, 56000, 1, 1);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 1, 9);

insert into ventas_factura values (DEFAULT, DATE '2019/07/05', 'Felipe');  /** id_factura: 2*/
insert into ventas_pagoscredito values (DEFAULT, '2345', DATE '2019/07/05', 'A', 100, 2);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 2, 2);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 2, 10);

insert into ventas_factura values (DEFAULT, DATE '2019/07/10', 'Felipe');  /** id_factura: 3*/
insert into ventas_pagoscredito values (DEFAULT, '3456', DATE '2019/07/10', 'A', 100, 3);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 3, 3);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 3, 11);

insert into ventas_factura values (DEFAULT, DATE '2019/07/12', 'Felipe');  /** id_factura: 4*/
insert into ventas_pagoscredito values (DEFAULT, '4567', DATE '2019/07/12', 'A', 100, 4);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 4, 4);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 4, 5);

insert into ventas_factura values (DEFAULT, DATE '2019/07/13', 'Felipe');  /** id_factura: 5*/
insert into ventas_pagoscredito values (DEFAULT, '5678', DATE '2019/07/13', 'A', 60, 5);
insert into ventas_pagosdebito values (DEFAULT, 1234, 1, TRUE, 40, 5);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 5, 6);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 5, 7);

insert into ventas_factura values (DEFAULT, DATE '2019/07/18', 'Felipe');  /** id_factura: 6*/
insert into ventas_pagoscredito values (DEFAULT, '6789', DATE '2019/07/18', 'A', 60, 6);
insert into ventas_pagosdebito values (DEFAULT, 1234, 2, TRUE, 40, 6);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 6, 8);

insert into ventas_factura values (DEFAULT, DATE '2019/07/18', 'Felipe');  /** id_factura: 7*/
insert into ventas_pagoscredito values (DEFAULT, '7890', DATE '2019/07/18', 'A', 10, 7);
insert into ventas_pagosdebito values (DEFAULT, 1234, 3, TRUE, 90, 7);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 7, 29);

insert into ventas_factura values (DEFAULT, DATE '2019/07/20', 'Felipe');  /** id_factura: 8*/
insert into ventas_pagosdebito values (DEFAULT, 1234, 4, TRUE, 100, 8);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 8, 30);

insert into ventas_factura values (DEFAULT, DATE '2019/07/22', 'Felipe');  /** id_factura: 9*/
insert into ventas_pagosdebito values (DEFAULT, 1234, 5, TRUE, 100, 9);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 9, 31);

insert into ventas_factura values (DEFAULT, DATE '2019/07/23', 'Felipe');  /** id_factura: 10*/
insert into ventas_pagosdebito values (DEFAULT, 1234, 6, TRUE, 100, 10);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 10, 32);



insert into ventas_factura values (DEFAULT, DATE '2019/07/02', 'Jaime');  /** id_factura: 11*/
insert into ventas_pagoscredito values (DEFAULT, '9012', DATE '2019/07/02', 'B', 20, 11);
insert into ventas_pagosdebito values (DEFAULT, 2345, 1, TRUE, 80, 11);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 11, 1);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 11, 9);

insert into ventas_factura values (DEFAULT, DATE '2019/07/03', 'Jaime');  /** id_factura: 12*/
insert into ventas_pagosdebito values (DEFAULT, 2345, 2, TRUE, 100, 12);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 12, 2);

insert into ventas_factura values (DEFAULT, DATE '2019/07/07', 'Jaime');  /** id_factura: 13*/
insert into ventas_pagosdebito values (DEFAULT, 2345, 3, TRUE, 100, 13);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 13, 3);

insert into ventas_factura values (DEFAULT, DATE '2019/07/08', 'Jaime');  /** id_factura: 14*/
insert into ventas_pagosdebito values (DEFAULT, 2345, 4, TRUE, 100, 14);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 14, 4);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 14, 5);



insert into ventas_factura values (DEFAULT, DATE '2019/07/01', 'Sara');  /** id_factura: 15*/
insert into ventas_pagosdebito values (DEFAULT, 3456, 1, TRUE, 100, 15);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 15, 13);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 15, 14);

insert into ventas_factura values (DEFAULT, DATE '2019/07/01', 'Sara');  /** id_factura: 16*/
insert into ventas_pagosdebito values (DEFAULT, 3456, 2, TRUE, 100, 16);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 16, 15);

insert into ventas_factura values (DEFAULT, DATE '2019/07/01', 'Sara');  /** id_factura: 17*/
insert into ventas_pagosdebito values (DEFAULT, 3456, 3, TRUE, 100, 17);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 17, 16);

insert into ventas_factura values (DEFAULT, DATE '2019/07/05', 'Sara');  /** id_factura: 18*/
insert into ventas_pagoscredito values (DEFAULT, '0123', DATE '2019/07/05', 'B', 40, 18);
insert into ventas_pagosdebito values (DEFAULT, 3456, 4, TRUE, 60, 18);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 18, 17);

insert into ventas_factura values (DEFAULT, DATE '2019/07/05', 'Sara');  /** id_factura: 19*/
insert into ventas_pagoscredito values (DEFAULT, '1324', DATE '2019/07/05', 'B', 40, 19);
insert into ventas_pagosdebito values (DEFAULT, 3456, 5, TRUE, 60, 19);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 19, 18);

insert into ventas_factura values (DEFAULT, DATE '2019/07/07', 'Sara');  /** id_factura: 20*/
insert into ventas_pagoscredito values (DEFAULT, '2436', DATE '2019/07/05', 'B', 40, 20);
insert into ventas_pagosdebito values (DEFAULT, 3456, 6, TRUE, 60, 20);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 20, 19);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 20, 20);

insert into ventas_factura values (DEFAULT, DATE '2019/07/07', 'Sara');  /** id_factura: 21*/
insert into ventas_pagoscredito values (DEFAULT, '3546', DATE '2019/07/05', 'B', 100, 21);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 21, 21);

insert into ventas_factura values (DEFAULT, DATE '2019/07/07', 'Sara');  /** id_factura: 22*/
insert into ventas_pagoscredito values (DEFAULT, '4657', DATE '2019/07/05', 'B', 40, 22);
insert into ventas_pagosdebito values (DEFAULT, 3456, 7, TRUE, 60, 22);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 22, 22);

insert into ventas_factura values (DEFAULT, DATE '2019/07/12', 'Sara');  /** id_factura: 23*/
insert into ventas_pagosdebito values (DEFAULT, 3456, 8, TRUE, 100, 23);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 23, 26);

insert into ventas_factura values (DEFAULT, DATE '2019/07/12', 'Sara');  /** id_factura: 24*/
insert into ventas_pagosdebito values (DEFAULT, 3456, 9, TRUE, 100, 24);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 24, 27);



insert into ventas_factura values (DEFAULT, DATE '2019/07/21', 'Natalia');  /** id_factura: 25*/
insert into ventas_pagosdebito values (DEFAULT, 4567, 1, TRUE, 100, 25);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 25, 13);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 25, 14);

insert into ventas_factura values (DEFAULT, DATE '2019/07/21', 'Natalia');  /** id_factura: 26*/
insert into ventas_pagosdebito values (DEFAULT, 4567, 2, TRUE, 100, 26);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 26, 15);

insert into ventas_factura values (DEFAULT, DATE '2019/07/21', 'Natalia');  /** id_factura: 27*/
insert into ventas_pagosdebito values (DEFAULT, 4567, 3, TRUE, 100, 27);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 27, 16);

insert into ventas_factura values (DEFAULT, DATE '2019/07/23', 'Natalia');  /** id_factura: 28*/
insert into ventas_pagoscredito values (DEFAULT, '1029', DATE '2019/07/23', 'B', 40, 28);
insert into ventas_pagosdebito values (DEFAULT, 4567, 4, TRUE, 60, 28);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 28, 17);

insert into ventas_factura values (DEFAULT, DATE '2019/07/23', 'Natalia');  /** id_factura: 29*/
insert into ventas_pagosdebito values (DEFAULT, 4567, 5, TRUE, 100, 29);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 29, 18);

insert into ventas_factura values (DEFAULT, DATE '2019/07/26', 'Natalia');  /** id_factura: 30*/
insert into ventas_pagosdebito values (DEFAULT, 4567, 6, TRUE, 100, 30);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 30, 19);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 30, 20);

insert into ventas_factura values (DEFAULT, DATE '2019/07/26', 'Natalia');  /** id_factura: 31*/
insert into ventas_pagosdebito values (DEFAULT, 4567, 7, TRUE, 100, 31);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 31, 23);

insert into ventas_factura values (DEFAULT, DATE '2019/07/26', 'Natalia');  /** id_factura: 32*/
insert into ventas_pagosdebito values (DEFAULT, 4567, 8, TRUE, 100, 32);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 32, 24);

insert into ventas_factura values (DEFAULT, DATE '2019/07/27', 'Natalia');  /** id_factura: 33*/
insert into ventas_pagosdebito values (DEFAULT, 4567, 9, TRUE, 100, 33);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 33, 25);

insert into ventas_factura values (DEFAULT, DATE '2019/07/29', 'Natalia');  /** id_factura: 34*/
insert into ventas_pagosdebito values (DEFAULT, 4567, 10, TRUE, 100, 34);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 34, 28);



insert into ventas_factura values (DEFAULT, DATE '2019/07/21', 'Maria Jose');  /** id_factura: 35*/
insert into ventas_pagosdebito values (DEFAULT, 5678, 1, TRUE, 100, 35);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 35, 13);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 35, 14);

insert into ventas_factura values (DEFAULT, DATE '2019/07/21', 'Maria Jose');  /** id_factura: 36*/
insert into ventas_pagosdebito values (DEFAULT, 5678, 2, TRUE, 100, 36);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 36, 15);

insert into ventas_factura values (DEFAULT, DATE '2019/07/21', 'Maria Jose');  /** id_factura: 37*/
insert into ventas_pagosdebito values (DEFAULT, 5678, 3, TRUE, 100, 37);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 37, 16);

insert into ventas_factura values (DEFAULT, DATE '2019/07/23', 'Maria Jose');  /** id_factura: 38*/
insert into ventas_pagoscredito values (DEFAULT, '2938', DATE '2019/07/23', 'C', 40, 38);
insert into ventas_pagosdebito values (DEFAULT, 5678, 4, TRUE, 60, 38);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 38, 17);

insert into ventas_factura values (DEFAULT, DATE '2019/07/23', 'Maria Jose');  /** id_factura: 39*/
insert into ventas_pagoscredito values (DEFAULT, '3847', DATE '2019/07/23', 'C', 20, 39);
insert into ventas_pagosdebito values (DEFAULT, 5678, 5, TRUE, 80, 39);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 39, 18);

insert into ventas_factura values (DEFAULT, DATE '2019/07/26', 'Maria Jose');  /** id_factura: 40*/
insert into ventas_pagoscredito values (DEFAULT, '4756', DATE '2019/07/26', 'C', 20, 40);
insert into ventas_pagosdebito values (DEFAULT, 5678, 6, TRUE, 80, 40);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 40, 19);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 40, 20);

insert into ventas_factura values (DEFAULT, DATE '2019/07/26', 'Maria Jose');  /** id_factura: 41*/
insert into ventas_pagosdebito values (DEFAULT, 5678, 7, TRUE, 100, 41);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 41, 23);

insert into ventas_factura values (DEFAULT, DATE '2019/07/26', 'Maria Jose');  /** id_factura: 42*/
insert into ventas_pagosdebito values (DEFAULT, 5678, 8, TRUE, 100, 42);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 42, 24);

insert into ventas_factura values (DEFAULT, DATE '2019/07/27', 'Maria Jose');  /** id_factura: 43*/
insert into ventas_pagosdebito values (DEFAULT, 5678, 9, TRUE, 100, 43);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 43, 25);

insert into ventas_factura values (DEFAULT, DATE '2019/07/29', 'Maria Jose');  /** id_factura: 44*/
insert into ventas_pagosdebito values (DEFAULT, 5678, 10, TRUE, 100, 44);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 44, 28);



insert into ventas_factura values (DEFAULT, DATE '2019/06/21', 'Camila');  /** id_factura: 45*/
insert into ventas_pagosdebito values (DEFAULT, 6789, 1, TRUE, 100, 45);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 45, 13);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 45, 14);

insert into ventas_factura values (DEFAULT, DATE '2019/06/21', 'Camila');  /** id_factura: 46*/
insert into ventas_pagosdebito values (DEFAULT, 6789, 2, TRUE, 100, 46);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 46, 15);

insert into ventas_factura values (DEFAULT, DATE '2019/06/21', 'Camila');  /** id_factura: 47*/
insert into ventas_pagosdebito values (DEFAULT, 6789, 3, TRUE, 100, 47);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 47, 16);

insert into ventas_factura values (DEFAULT, DATE '2019/06/23', 'Camila');  /** id_factura: 48*/
insert into ventas_pagosdebito values (DEFAULT, 6789, 4, TRUE, 100, 48);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 48, 17);

insert into ventas_factura values (DEFAULT, DATE '2019/06/23', 'Camila');  /** id_factura: 49*/
insert into ventas_pagosdebito values (DEFAULT, 6789, 5, TRUE, 100, 49);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 49, 18);

insert into ventas_factura values (DEFAULT, DATE '2019/06/26', 'Camila');  /** id_factura: 50*/
insert into ventas_pagosdebito values (DEFAULT, 6789, 6, TRUE, 100, 50);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 50, 19);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 50, 20);

insert into ventas_factura values (DEFAULT, DATE '2019/06/26', 'Camila');  /** id_factura: 51*/
insert into ventas_pagosdebito values (DEFAULT, 6789, 7, TRUE, 100, 51);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 51, 23);

insert into ventas_factura values (DEFAULT, DATE '2019/06/26', 'Camila');  /** id_factura: 52*/
insert into ventas_pagosdebito values (DEFAULT, 6789, 8, TRUE, 100, 52);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 52, 24);

insert into ventas_factura values (DEFAULT, DATE '2019/06/27', 'Camila');  /** id_factura: 53*/
insert into ventas_pagosdebito values (DEFAULT, 6789, 9, TRUE, 100, 53);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 53, 25);

insert into ventas_factura values (DEFAULT, DATE '2019/06/29', 'Camila');  /** id_factura: 54*/
insert into ventas_pagosdebito values (DEFAULT, 6789, 10, TRUE, 100, 54);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 54, 28);



insert into ventas_factura values (DEFAULT, DATE '2019/06/19', 'Laura');  /** id_factura: 55*/
insert into ventas_pagosdebito values (DEFAULT, 7890, 1, TRUE, 100, 55);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 55, 13);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 55, 14);

insert into ventas_factura values (DEFAULT, DATE '2019/06/19', 'Laura');  /** id_factura: 56*/
insert into ventas_pagosdebito values (DEFAULT, 7890, 2, TRUE, 100, 56);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 56, 15);

insert into ventas_factura values (DEFAULT, DATE '2019/06/19', 'Laura');  /** id_factura: 57*/
insert into ventas_pagosdebito values (DEFAULT, 7890, 3, TRUE, 100, 57);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 57, 16);

insert into ventas_factura values (DEFAULT, DATE '2019/06/23', 'Laura');  /** id_factura: 58*/
insert into ventas_pagosdebito values (DEFAULT, 7890, 4, TRUE, 100, 58);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 58, 17);

insert into ventas_factura values (DEFAULT, DATE '2019/06/23', 'Laura');  /** id_factura: 59*/
insert into ventas_pagosdebito values (DEFAULT, 7890, 5, TRUE, 100, 59);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 59, 18);

insert into ventas_factura values (DEFAULT, DATE '2019/06/26', 'Laura');  /** id_factura: 60*/
insert into ventas_pagosdebito values (DEFAULT, 7890, 6, TRUE, 100, 60);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 60, 19);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 60, 20);

insert into ventas_factura values (DEFAULT, DATE '2019/06/26', 'Laura');  /** id_factura: 61*/
insert into ventas_pagosdebito values (DEFAULT, 7890, 7, TRUE, 100, 61);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 61, 23);

insert into ventas_factura values (DEFAULT, DATE '2019/06/26', 'Laura');  /** id_factura: 62*/
insert into ventas_pagosdebito values (DEFAULT, 7890, 8, TRUE, 100, 62);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 62, 24);

insert into ventas_factura values (DEFAULT, DATE '2019/06/27', 'Laura');  /** id_factura: 63*/
insert into ventas_pagosdebito values (DEFAULT, 7890, 9, TRUE, 100, 63);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 63, 25);

insert into ventas_factura values (DEFAULT, DATE '2019/06/29', 'Laura');  /** id_factura: 64*/
insert into ventas_pagosdebito values (DEFAULT, 7890, 10, TRUE, 100, 64);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 64, 28);



insert into ventas_factura values (DEFAULT, DATE '2019/05/19', 'Marcela');  /** id_factura: 65*/
insert into ventas_pagoscredito values (DEFAULT, '0897', DATE '2019/05/19', 'C', 20, 65);
insert into ventas_pagosdebito values (DEFAULT, 1324, 1, TRUE, 80, 65);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 65, 13);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 65, 14);

insert into ventas_factura values (DEFAULT, DATE '2019/05/19', 'Marcela');  /** id_factura: 66*/
insert into ventas_pagoscredito values (DEFAULT, '0897', DATE '2019/05/19', 'C', 45, 66);
insert into ventas_pagosdebito values (DEFAULT, 1324, 2, TRUE, 55, 66);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 66, 15);

insert into ventas_factura values (DEFAULT, DATE '2019/05/19', 'Marcela');  /** id_factura: 67*/
insert into ventas_pagoscredito values (DEFAULT, '0897', DATE '2019/05/19', 'C', 45, 67);
insert into ventas_pagosdebito values (DEFAULT, 1324, 3, TRUE, 55, 67);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 67, 16);

insert into ventas_factura values (DEFAULT, DATE '2019/05/23', 'Marcela');  /** id_factura: 68*/
insert into ventas_pagosdebito values (DEFAULT, 1324, 4, TRUE, 100, 68);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 68, 17);

insert into ventas_factura values (DEFAULT, DATE '2019/05/23', 'Marcela');  /** id_factura: 69*/
insert into ventas_pagosdebito values (DEFAULT, 1324, 5, TRUE, 100, 69);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 69, 18);

insert into ventas_factura values (DEFAULT, DATE '2019/05/26', 'Marcela');  /** id_factura: 70*/
insert into ventas_pagosdebito values (DEFAULT, 1324, 6, TRUE, 100, 70);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 70, 19);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 70, 20);

insert into ventas_factura values (DEFAULT, DATE '2019/05/26', 'Marcela');  /** id_factura: 71*/
insert into ventas_pagosdebito values (DEFAULT, 1324, 7, TRUE, 100, 71);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 71, 23);

insert into ventas_factura values (DEFAULT, DATE '2019/05/26', 'Marcela');  /** id_factura: 72*/
insert into ventas_pagosdebito values (DEFAULT, 1324, 8, TRUE, 100, 72);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 72, 24);

insert into ventas_factura values (DEFAULT, DATE '2019/05/27', 'Marcela');  /** id_factura: 73*/
insert into ventas_pagosdebito values (DEFAULT, 1324, 9, TRUE, 100, 73);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 73, 25);

insert into ventas_factura values (DEFAULT, DATE '2019/05/29', 'Marcela');  /** id_factura: 74*/
insert into ventas_pagosdebito values (DEFAULT, 1324, 10, TRUE, 100, 74);
insert into ventas_detallesfactura values (DEFAULT, 1, 28000, 74, 28);

BEGIN;
SELECT setval(pg_get_serial_sequence('"usuarios_administradorduenio"','pkAdministradorDuenio'), coalesce(max("pkAdministradorDuenio"), 1), max("pkAdministradorDuenio") IS NOT null) FROM "usuarios_administradorduenio";
SELECT setval(pg_get_serial_sequence('"usuarios_carrito"','pkCarrito'), coalesce(max("pkCarrito"), 1), max("pkCarrito") IS NOT null) FROM "usuarios_carrito";
COMMIT;

BEGIN;
SELECT setval(pg_get_serial_sequence('"inventario_categoria"','pkCategoria'), coalesce(max("pkCategoria"), 1), max("pkCategoria") IS NOT null) FROM "inventario_categoria";
SELECT setval(pg_get_serial_sequence('"inventario_subcategoria"','pkSubCategoria'), coalesce(max("pkSubCategoria"), 1), max("pkSubCategoria") IS NOT null) FROM "inventario_subcategoria";
SELECT setval(pg_get_serial_sequence('"inventario_producto"','pkProducto'), coalesce(max("pkProducto"), 1), max("pkProducto") IS NOT null) FROM "inventario_producto";
SELECT setval(pg_get_serial_sequence('"inventario_bodega"','pkBodega'), coalesce(max("pkBodega"), 1), max("pkBodega") IS NOT null) FROM "inventario_bodega";
SELECT setval(pg_get_serial_sequence('"inventario_detallesproducto"','pkDetallesP'), coalesce(max("pkDetallesP"), 1), max("pkDetallesP") IS NOT null) FROM "inventario_detallesproducto";
COMMIT;

BEGIN;
SELECT setval(pg_get_serial_sequence('"ventas_descuentoproducto"','pkDescuentoProducto'), coalesce(max("pkDescuentoProducto"), 1), max("pkDescuentoProducto") IS NOT null) FROM "ventas_descuentoproducto";
SELECT setval(pg_get_serial_sequence('"ventas_descuentocategoria"','pkDescuentoCategoria'), coalesce(max("pkDescuentoCategoria"), 1), max("pkDescuentoCategoria") IS NOT null) FROM "ventas_descuentocategoria";
SELECT setval(pg_get_serial_sequence('"ventas_descuentosubcategoria"','pkDescuentoSubCategoria'), coalesce(max("pkDescuentoSubCategoria"), 1), max("pkDescuentoSubCategoria") IS NOT null) FROM "ventas_descuentosubcategoria";
SELECT setval(pg_get_serial_sequence('"ventas_factura"','pkFactura'), coalesce(max("pkFactura"), 1), max("pkFactura") IS NOT null) FROM "ventas_factura";
SELECT setval(pg_get_serial_sequence('"ventas_detallesfactura"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "ventas_detallesfactura";
SELECT setval(pg_get_serial_sequence('"ventas_pagoscredito"','pkPagosCredito'), coalesce(max("pkPagosCredito"), 1), max("pkPagosCredito") IS NOT null) FROM "ventas_pagoscredito";
SELECT setval(pg_get_serial_sequence('"ventas_pagosdebito"','pkPagosDebito'), coalesce(max("pkPagosDebito"), 1), max("pkPagosDebito") IS NOT null) FROM "ventas_pagosdebito";
COMMIT;
