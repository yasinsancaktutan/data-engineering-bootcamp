-- 7a (execution: 1 m 56 s 699 ms, fetching: 54 ms)
select * from (
           select tconst, nconst
           from `title.principals`
           where category in ('actor', 'actress') #oyuncular
       ) o
inner join (

select     tconst, nconst
           from `title.principals`
           where category in ('director') #yönetmenler


) y on y.tconst = o.tconst and y.nconst = o.nconst
inner join `title.basic` b on b.tconst = y.tconst
where b.startYear between 2000 and 2010