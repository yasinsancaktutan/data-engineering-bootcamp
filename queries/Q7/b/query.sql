#7b (execution: 1 m 25 s 508 ms, fetching: 221 ms)

select distinct nb.primaryName from (
           select tconst, nconst
           from `title.principals`
           where category = 'actress' #aktrisler
       ) o
inner join (

select     tconst, nconst
           from `title.principals`
           where category = 'composer' #müzik departmanı


) y on y.nconst = o.nconst
inner join `title.basic` b on b.tconst = y.tconst
inner join `name.basics` nb on nb.nconst = o.nconst
where b.startYear between 2000 and YEAR(CURDATE());