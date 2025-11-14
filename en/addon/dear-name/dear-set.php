<?php

			if ( $call_company !== '' ) {
				$thanks_body_head .= $call_company.PHP_EOL;
			}
			
			if ( $call_name !== '' ) {
				$thanks_body_head .= $call_name.' 様'.PHP_EOL;
			}
			
			if ( $call_company !== '' || $call_name !== '' ) {
				$this->thanks_body  = $thanks_body_head.$this->thanks_body;
			}
