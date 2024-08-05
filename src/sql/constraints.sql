alter table tractors
    add CONSTRAINT pk_tractors_is PRIMARY KEY(id),
    alter column id set not null,
    alter column model set not null,
    alter column release_year set not null,
    alter column enginetype set not null,
    alter column enginetype set not null, 
    alter column enginepower set not null, 
    alter column fronttiresize set not null, 
    alter column backtiresize set not null, 
    alter column wheelsamount set not null, 
    alter column tankcapacity set not null, 
    alter column ecologicalstandart set not null, 
    alter column length set not null, 
    alter column cabinheight set not null, 
    alter column width set not null;


alter table assemblylines
    add CONSTRAINT pk_assembly_line PRIMARY key(id),
    alter column id set not null, 
    alter column name set not null, 
    alter column length set not null, 
    alter column width set not null, 
    alter column height set not null, 
    alter column status set not null, 
    alter column production set not null, 
    alter column downtime set not null, 
    alter column inspectionsamountperyear set not null, 
    alter column lastinspectiondate set not null, 
    alter column nextinspectiondate set not null, 
    alter column defectrate set not null;

alter table users 
    add CONSTRAINT pk_usersid PRIMARY key(id),
    alter column id set not null, 
    alter column name set not null, 
    alter column surname set not null, 
    alter column fatherame set not null, 
    alter column department set not null, 
    alter column email set not null, 
    alter column password set not null, 
    alter column dateofbirth set not null, 
    alter column sex set not null, 
    alter column role set not null;

alter table details 
    add CONSTRAINT pk_details PRIMARY key(id),
    alter column id set not null, 
    alter column name set not null, 
    alter column country set not null, 
    alter column amount set not null, 
    alter column price set not null, 
    alter column length set not null, 
    alter column width set not null, 
    alter column height set not null;

alter table servicerequests
    add CONSTRAINT pk_requestid PRIMARY key(id),
    alter column id set not null, 
    add CONSTRAINT fk_lineid_servicerequests FOREIGN key (lineid) REFERENCES assemblylines(id) on DELETE CASCADE,
    add CONSTRAINT fk_userid_servicerequests FOREIGN key (userid) REFERENCES users(id) on delete cascade,
    alter column lineid set not null,  
    alter column userid set not null, 
    alter column requestdate set not null, 
    alter column status set not null, 
    alter column type set not null, 
    alter column description set not null;

alter table detailorders
    add CONSTRAINT pk_detaleorders PRIMARY key(id), 
    alter column id set not null, 
    add CONSTRAINT fk_userid_detailorders FOREIGN key (userid) REFERENCES users(id) on delete cascade,
    add CONSTRAINT fk_requestid_detailorders FOREIGN key (requestid) REFERENCES servicerequests(id) on delete cascade,
    alter column userid set not null, 
    alter column requestid set not null, 
    alter column status set not null, 
    alter column totalprice set not null, 
    alter column orderdate set not null;

alter table servicereports
    add CONSTRAINT pk_reporttid PRIMARY key(id),
    alter column id set not null, 
    add CONSTRAINT fk_lineid_servicereports FOREIGN key (lineid) REFERENCES assemblylines(id) on DELETE CASCADE,
    add CONSTRAINT fk_userid_servicereports FOREIGN key (userid) REFERENCES users(id) on delete cascade,
    add CONSTRAINT fk_requestid_servicerequests FOREIGN key (requestid) REFERENCES servicerequests(id) on delete cascade,
    alter column lineid set not null, 
    alter column userid set not null, 
    alter column requestid set not null, 
    alter column opendate set not null, 
    alter column closedate set not null, 
    alter column totalprice set not null, 
    alter column description set not null;

alter table order_detail
    add CONSTRAINT fk_orderid_order_detail FOREIGN key (orderid) REFERENCES detailorders(id) on DELETE CASCADE,
    add CONSTRAINT fk_detailid_order_detail FOREIGN key (detailid) REFERENCES details(id) on DELETE CASCADE,
    alter column orderid set not null, 
    alter column detailid set not null, 
    alter column detailsamount set not null,
    add constraint pk_order_detail primary key(orderid, detailid);

alter table tractor_line
    add CONSTRAINT fk_tractorid_tractor_line FOREIGN key (tractorid) REFERENCES tractors(id) on DELETE CASCADE,
    add CONSTRAINT fk_lineid_tractorline FOREIGN key (lineid) REFERENCES assemblylines(id) on DELETE CASCADE,
    add constraint pk_tractor_line primary key(tractorid, lineid);


alter table line_detail
    add CONSTRAINT fk_lineid_line_detail FOREIGN key (lineid) REFERENCES assemblylines(id) on DELETE CASCADE,
    add CONSTRAINT fk_detaleid_line_detail FOREIGN key (detailid) REFERENCES details(id) on delete cascade,
    add constraint pk_line_detail primary key(lineid, detailid);