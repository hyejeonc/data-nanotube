set mode load
if { $mode == "load" } {
   set init [mol new atoms 1]
   set sel  [atomselect $init all]
   $sel set name 1
   $sel set name 2
   $sel set name 3
   $sel set name 4
   $sel delete
   mol delete $init
   mol delete all
   display update off
   set filelist [lsort -dictionary [glob cylinder_shell.*.vtf]]
   set filecount 0
   foreach file [split $filelist] {incr filecount}
   if { $filecount > 1 } {
      puts "Which vtf-file would you like to load? Enter number ..."
      for {set i 0} {$i < $filecount} {incr i} {
         set txfile($i) [lindex [split $filelist] $i]
         puts "$i) $txfile($i)"
      }
      puts "$i) load all"
      gets stdin choice
      if { $choice == $i } {
         for {set i 0} {$i < $filecount} {incr i} {
            mol addfile $txfile($i) type vtf first 0 last 0 autobonds off
         }
      } else {
         set project $txfile($choice)
         mol load vtf $project
      }
   } else {
      set project $filelist
      mol load vtf $project
   }
   color Display Background white
   color Axes Labels black
   display depthcue off
   set molID [molinfo top]
   mol delrep 0 $molID
    mol representation VDW 1.0  20.0
   mol addrep $molID
    mol representation Bonds 0.30  12.0
   mol addrep $molID
   color change rgb   31 1.000 0.000 0.000
   color Name  1   31
   color change rgb   30 0.000 1.000 0.000
   color Name  2   30
   color change rgb   29 0.000 0.000 1.000
   color Name  3   29
   color change rgb   28 0.000 1.000 1.000
   color Name  4   28
   mol load graphics frame
   set frameID [molinfo top]
   mol top $molID
   graphics $frameID color black
   set len    600.0
   set rad    800.0
   for {set i 0} {$i < 157} {incr i} {
      set x1 [expr { $rad*cos(0.04*$i) }]
      set y1 [expr { $rad*sin(0.04*$i) }]
      set x2 [expr { $rad*cos(0.04*($i+1)) }]
      set y2 [expr { $rad*sin(0.04*($i+1)) }]
      graphics $frameID line "$x1 $y1  $len" "$x2 $y2  $len" width 2 style solid
      graphics $frameID line "$x1 $y1 -$len" "$x2 $y2 -$len" width 2 style solid
   }
   foreach i {0.0 0.7854 1.5708 2.3562 3.1416 3.9270 4.7124 5.4978} {
      set x [expr { $rad*cos($i) }]
      set y [expr { $rad*sin($i) }]
      graphics $frameID line "$x  $y $len" "$x  $y -$len" width 1 style dashed
   }
   display update on
}
